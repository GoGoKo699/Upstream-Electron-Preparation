#!/usr/bin/env python3
"""Finite-energy quantum fidelity in the fixed one-input fractionalization model.

Run: python check_finite_accuracy.py --output NEW.json
Only exact identities, small fermionic matrices, and 1D quadratures are used.
No previous result is overwritten. All-size optimality is proved in SCOUT_09.md.
"""
from __future__ import annotations
import argparse
from functools import lru_cache
import json
from math import pi
from pathlib import Path
import unittest
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import jv
import sympy as sp

REPORT:dict[str,object]={}


def transfer(x,p=.5):
    return p+(1-p)*np.exp(1j*np.asarray(x))


def optimum(x,mu,a,p=.5):
    """A=vhat/(2pi), x=omega*tau, a=2w/tau. Real drive uses Hermitian extension."""
    H=transfer(x,p)
    return H.conjugate()*np.exp(-a*np.asarray(x)/2)/(abs(H)**2+mu*np.asarray(x))


def residue_coefficient(a:float):
    if a<=0:raise ValueError('Positive target-width ratio required.')
    count=max(8,int(np.ceil(40/(2*pi*a))))
    z=(2*np.arange(count)+1)*pi
    B=float(pi*np.sum(np.exp(-a*z)/np.sqrt(z)))
    first=(2*count+1)*pi
    tail=pi*np.exp(-a*first)/(np.sqrt(first)*(-np.expm1(-2*pi*a)))
    return B,a*B*B,float(tail)


@lru_cache(None)
def frontier(mu:float,a:float,p:float=.5,tol:float=3e-11):
    """Pole-aware integration with a conservative bound on omitted frequencies.

    QUADPACK errors are diagnostic estimates, not interval-certified roundoff bounds.
    The infinite tail bound is analytic. No cutoff turns a pole into a finite cost.
    """
    if not (mu>0 and a>0 and 0<=p<=1):
        raise ValueError('Use mu>0, a>0, 0<=p<=1.')
    d=abs(2*p-1)
    exponent=max(45.,np.log(1/mu)+32.)
    cells=max(2,int(np.ceil(exponent/(2*pi*a))))
    U=D=Eout=err=0.
    for k in range(cells):
        zero=(2*k+1)*pi
        scale=2*np.sqrt(mu*zero+d*d)
        # Geometric subdivision resolves the narrow notch without a tangent-map
        # endpoint boundary layer. No quadrature warnings are suppressed.
        cuts=[0.,min(scale,pi)]
        while cuts[-1]<pi:cuts.append(min(2*cuts[-1],pi))
        def integrand(s,which):
            x=zero+s
            h=np.sin(s/2)**2+d*d*np.cos(s/2)**2
            den=h+mu*x
            base=np.exp(-a*x)/(den*den)
            return (h if which==0 else mu*mu*x if which==1 else h*h)*base
        values=[]
        for j in range(3):
            value=0.
            for low,high in zip(cuts[:-1],cuts[1:]):
                left=quad(lambda s:integrand(s,j),-high,-low,epsabs=tol,epsrel=tol,limit=160)
                right=quad(lambda s:integrand(s,j),low,high,epsabs=tol,epsrel=tol,limit=160)
                value+=left[0]+right[0];err+=left[1]+right[1]
            values.append(value)
        U+=values[0];D+=values[1];Eout+=values[2]
    cutoff=2*pi*cells
    tail_R=np.exp(-a*cutoff)/(4*mu*cutoff)
    tail_D=np.exp(-a*cutoff)/(a*cutoff)
    return dict(mu=mu,a=a,p=p,energy_ratio=a*U,infidelity_exponent=D,
                fidelity=float(np.exp(-D)),selected_output_energy_ratio=a*Eout,
                other_output_energy_ratio=a*(U-Eout),frequency_cutoff=cutoff,
                energy_tail_bound=float(tail_R),exponent_tail_bound=float(tail_D),
                quadrature_error_estimate=float(err))


@lru_cache(None)
def at_fidelity(F:float,a:float,p:float=.5):
    if not 0<F<1:raise ValueError('Use a fidelity strictly between zero and one.')
    target=-np.log(F)
    center=-5.;lo=hi=center
    while frontier(np.exp(lo),a,p)['infidelity_exponent']>target:lo-=4
    while frontier(np.exp(hi),a,p)['infidelity_exponent']<target:hi+=4
    root=brentq(lambda y:frontier(float(np.exp(y)),a,p)['infidelity_exponent']-target,
                lo,hi,xtol=2e-11)
    return frontier(float(np.exp(root)),a,p)


class FiniteAccuracyChecks(unittest.TestCase):
    def test_quantum_overlap_normalization_and_charge(self):
        rows=[]
        for w,W,t in ((.5,.5,0.),(.5,1.,0.),(.3,.8,.6),(1.,.4,-1.3)):
            def integrand(q):
                if q==0:return 0.
                d=np.exp(-w*q)-np.exp(-W*q+1j*t*q)
                return abs(d)**2/q
            D=quad(integrand,0,np.inf,epsabs=2e-12,epsrel=2e-12)[0]
            exact=4*w*W/((w+W)**2+t*t)
            # Independent normalized energy-space one-electron wavefunctions.
            fun=lambda q:2*np.sqrt(w*W)*np.exp(-(w+W)*q+1j*t*q)
            ov=quad(lambda q:fun(q).real,0,np.inf,epsabs=2e-12)[0]+1j*quad(lambda q:fun(q).imag,0,np.inf,epsabs=2e-12)[0]
            self.assertLess(abs(np.exp(-D)-exact),2e-12)
            self.assertLess(abs(abs(ov)**2-exact),2e-12)
            energy=quad(lambda x:(2*w/(x*x+w*w))**2,-np.inf,np.inf,epsabs=2e-11)[0]/(4*pi)
            self.assertAlmostEqual(energy,1/(2*w),places=11)
            rows.append(dict(width=w,comparison_width=W,time_shift=t,coherent_fidelity=np.exp(-D),orbital_fidelity=abs(ov)**2,exact=exact))
        for a in (.25,1.,2.):
            for mu in (1e-5,.01,.4):self.assertEqual(optimum(0.,mu,a),1+0j)
        REPORT['charged_sector_normalization']=dict(rows=rows,dc_amplitude_is_one=True,
          scope='Equal-charge relative coherent displacement, not overlap of a charged pulse with the uncharged bosonic vacuum.')

    def test_fermionic_determinants_holes_and_probability(self):
        rows=[]
        # Neutral single-harmonic phase on a circle: an independent algebra benchmark.
        # Occupied negative modes and initially empty positive modes; no spurious
        # bottom Fermi edge from a finite filled sea is introduced.
        for amplitude in (.2,1.,2.):
            vals=[]
            for cutoff in (20,40):
                m=np.arange(1,cutoff+1)[:,None];q=np.arange(cutoff)[None,:]
                cross=1j**(-m-q)*jv(-m-q,amplitude)
                holes=cross@cross.conjugate().T
                ev=np.linalg.eigvalsh(holes)
                sign,logF=np.linalg.slogdet(np.eye(cutoff)-holes)
                self.assertLess(abs(sign-1),2e-14)
                F=float(np.exp(logF));D=amplitude*amplitude/4
                self.assertLess(abs(F-np.exp(-D)),3e-13)
                self.assertLessEqual(float(np.trace(holes).real),D+2e-13)
                self.assertGreaterEqual(ev.min(),-1e-14)
                vals.append(dict(cutoff=cutoff,fidelity=F,mean_holes=float(np.trace(holes).real)))
            rows.append(dict(phase_amplitude=amplitude,coherent_exponent=amplitude**2/4,checks=vals))
        rng=np.random.default_rng(913)
        for _ in range(50):
            probabilities=rng.uniform(0,.7,size=7)
            F=np.prod(1-probabilities);D=-np.log(F)
            self.assertLessEqual(probabilities.sum(),D)
        # A second finite-circle check uses the actual optimized error waveform.
        # The target phase is removed first, so the remaining drive is neutral.
        optimized=[]
        for step in (.2,.1):
            cutoff=256;frequency=step*np.arange(1,cutoff+1)
            mu=.05;a=1.;h=np.cos(frequency/2)**2
            error=-mu*frequency*np.exp(-a*frequency/2)/(h+mu*frequency)
            phase_coeff=1j*error/np.arange(1,cutoff+1)
            nt=8192;arr=np.zeros(nt,complex)
            arr[1:cutoff+1]=phase_coeff;arr[-cutoff:]=phase_coeff[::-1].conjugate()
            phase=np.fft.fft(arr).real
            unitary_coeff=np.fft.ifft(np.exp(-1j*phase))
            m=np.arange(1,cutoff+1)[:,None];q=np.arange(cutoff)[None,:]
            cross=unitary_coeff[(-m-q)%nt]
            holes=cross@cross.conjugate().T
            sign,logF=np.linalg.slogdet(np.eye(cutoff)-holes)
            Dc=float(np.sum(abs(error)**2/np.arange(1,cutoff+1)))
            Fc=float(np.exp(-Dc));Fd=float(np.exp(logF))
            self.assertLess(abs(sign-1),1e-12)
            self.assertLess(abs(Fc-Fd),2e-11)
            self.assertLessEqual(float(np.trace(holes).real),Dc+2e-11)
            optimized.append(dict(frequency_step=step,fermionic_cutoff=cutoff,
                coherent_fidelity=Fc,determinant_fidelity=Fd,
                neutral_error_mean_holes=float(np.trace(holes).real),
                circle_exponent=Dc,continuum_exponent=frontier(mu,a)['infidelity_exponent']))
        self.assertLess(abs(optimized[1]['circle_exponent']-optimized[1]['continuum_exponent']),
                        abs(optimized[0]['circle_exponent']-optimized[0]['continuum_exponent']))
        REPORT['optimized_error_fermionic_check']=dict(rows=optimized,
            scope='Finite-circle regularization of the neutral relative phase; continuum optimality and the physical charged-state hole inequality are proved separately.')
        REPORT['fermionic_crosscheck']=dict(neutral_phase_benchmark=rows,
          bound='N_h + 1 - n_target <= -log F for the charged target; probability of any holes <= 1-F.',
          scope='The finite circle benchmark tests coherent/Slater normalization; it is not a substitute for the finite-pulse theorem.')

    def test_global_optimality_completion_and_monotonicity(self):
        hr,hi,ar,ai,f,x,mu=sp.symbols('hr hi ar ai f x mu',real=True)
        h=hr*hr+hi*hi;den=h+mu*x
        lhs=((hr*ar-hi*ai-f)**2+(hr*ai+hi*ar)**2)/x+mu*(ar*ar+ai*ai)
        center_r=hr*f/den;center_i=-hi*f/den
        rhs=mu*f*f/den+(h/x+mu)*((ar-center_r)**2+(ai-center_i)**2)
        self.assertEqual(sp.cancel(lhs-rhs),0)
        rows=[]
        for a in (.25,1.,2.):
            v=[frontier(mu,a) for mu in (1e-5,1e-3,.1)]
            self.assertTrue(all(v[i]['energy_ratio']>v[i+1]['energy_ratio'] for i in range(2)))
            self.assertTrue(all(v[i]['infidelity_exponent']<v[i+1]['infidelity_exponent'] for i in range(2)))
            m=.007;eps=1e-4
            lo,hi=frontier(m*(1-eps),a),frontier(m*(1+eps),a)
            slope=(hi['infidelity_exponent']-lo['infidelity_exponent'])/(hi['energy_ratio']-lo['energy_ratio'])
            self.assertLess(abs(slope+m/a),2e-9)
            rows.append(dict(a=a,frontier=v,observed_dD_dR=slope,analytic_dD_dR=-m/a))
        REPORT['global_quadratic_optimum']=dict(completion_exact=True,monotonicity=rows,
          scope='Completion of the square proves all-input optimum; sampled points only check evaluation.')

    def test_independent_frequency_quadrature_and_energy_conservation(self):
        rows=[]
        for mu,a,p in ((1e-3,1.,.5),(.05,.25,.5),(.02,2.,.55)):
            r=frontier(mu,a,p);cut=r['frequency_cutoff']
            breaks=np.arange(0,cut+.1,pi)
            ds=[]
            for which in range(3):
                def f(x):
                    H=transfer(x,p);A=optimum(x,mu,a,p);target=np.exp(-a*x/2)
                    return abs(A)**2 if which==0 else abs(H*A-target)**2/x if which==1 and x else abs(H*A)**2 if which==2 else 0.
                value=sum(quad(f,l,h,epsabs=3e-12,epsrel=3e-11,limit=160)[0] for l,h in zip(breaks[:-1],breaks[1:]))
                ds.append(value)
            self.assertLess(abs(a*ds[0]-r['energy_ratio']),2e-9)
            self.assertLess(abs(ds[1]-r['infidelity_exponent']),2e-11)
            self.assertLess(abs(a*ds[2]-r['selected_output_energy_ratio']),2e-10)
            self.assertGreaterEqual(r['other_output_energy_ratio'],-1e-13)
            self.assertLess(r['energy_tail_bound'],2e-12)
            rows.append(dict(mu=mu,a=a,p=p,pole_aware=r,direct_values=ds))
        REPORT['quadrature_and_energy']=rows

    def test_high_fidelity_asymptotic_and_width_dependence(self):
        rows=[]
        for a in (.25,.5,1.):
            B,C,tail=residue_coefficient(a)
            seq=[]
            for mu in (1e-5,1e-7,1e-9):
                r=frontier(mu,a)
                seq.append(dict(mu=mu,scaled_R=r['energy_ratio']*np.sqrt(mu)/(a*B),
                    scaled_D=r['infidelity_exponent']/(B*np.sqrt(mu)),
                    product=r['energy_ratio']*r['infidelity_exponent'],asymptotic_product=C))
            self.assertLess(abs(seq[-1]['product']/C-1),.003)
            self.assertLess(abs(seq[-1]['scaled_D']-1),3e-5)
            self.assertLess(abs(seq[-1]['scaled_R']-1),.003)
            self.assertLess(abs(seq[-1]['product']/C-1),abs(seq[0]['product']/C-1))
            self.assertLess(tail,1e-15)
            rows.append(dict(a=a,B=B,C=C,samples=seq))
        x=sp.symbols('x',real=True)
        self.assertEqual(sp.integrate(x*x/(1+x*x)**2,(x,-sp.oo,sp.oo)),sp.pi/2)
        self.assertEqual(sp.integrate(1/(1+x*x)**2,(x,-sp.oo,sp.oo)),sp.pi/2)
        REPORT['residue_asymptotic']=rows

    def test_fixed_fidelity_costs_and_no_finite_accuracy_transition(self):
        rows=[]
        for a in (.25,.5,1.,2.):
            for F in (.99,.999):
                r=at_fidelity(F,a)
                self.assertLess(abs(r['fidelity']-F),2e-11)
                self.assertLess(r['energy_tail_bound'],2e-11)
                refined=frontier(r['mu'],a,.5,5e-12)
                self.assertLess(abs(r['energy_ratio']-refined['energy_ratio']),2e-8)
                rows.append(dict(target_fidelity=F,target_width_over_delay=a/2,
                    optimal_input_energy_over_target=r['energy_ratio'],mu=r['mu'],
                    mean_hole_bound=-np.log(F),any_hole_probability_bound=1-F))
        self.assertGreater(at_fidelity(.999,.25)['energy_ratio'],200)
        self.assertLess(at_fidelity(.999,2.)['energy_ratio'],1.2)
        base=at_fidelity(.999,1.,.5)
        close=at_fidelity(.999,1.,.50001)
        self.assertLess(abs(close['energy_ratio']/base['energy_ratio']-1),1e-5)
        broad=at_fidelity(.99,2.)
        self.assertLess(broad['energy_ratio'],1.) # approximate target energy need not equal exact-target energy
        REPORT['finite_fidelity_table']=rows
        REPORT['equal_mixing_continuity']=dict(equal=base,slightly_imbalanced=close,
          scope='Continuity at fixed nonzero error; no contradiction with diverging exact-target energy.')

    def test_reference_controls_and_metric_warning(self):
        # The single allowed input is a resource assumption: two controllable inputs
        # invert the full unitary scattering matrix with the target energy exactly.
        for p in (.1,.5,.8):
            for x in (0.,.4,pi,3*pi,7.):
                z=np.exp(1j*x);c=np.sqrt(p*(1-p))
                S=np.array([[p+(1-p)*z,c*(1-z)],[c*(1-z),(1-p)+p*z]])
                target=np.array([np.exp(-x/2),0.])
                vin=S.conjugate().T@target
                self.assertLess(np.linalg.norm(S@vin-target),5e-16)
                self.assertLess(abs(np.vdot(vin,vin)-np.vdot(target,target)),5e-16)
        # Hole-free pulses can have arbitrarily low overlap with the specified target.
        for ratio in (10,100,1000):
            F=4*ratio/(1+ratio)**2
            self.assertLess(F,1.)
        # Charge-mismatched comparison has logarithmically divergent infrared cost.
        cut1,cut2=1e-3,1e-6
        diff=quad(lambda x:np.exp(-x)/x,cut2,cut1,epsabs=1e-11)[0]
        self.assertGreater(diff,6.9)
        REPORT['scope_controls']=dict(two_inputs_exact=True,
          charge_difference_forces_orthogonality=True,
          hole_free_is_not_target_fidelity=True,
          no_hole_minimization_claim=True,
          bandwidth_temperature_duration_and_calibration_unconstrained=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.output and args.output.exists():parser.error(f'Refusing existing output {args.output}')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(FiniteAccuracyChecks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',tests_run=result.testsRun,
       scope='Exact identities and small quadrature/matrix diagnostics; no independent review, exact numerical interval certificates, or implemented device.')
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        with args.output.open('x',encoding='utf-8') as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)

if __name__=='__main__':main()
