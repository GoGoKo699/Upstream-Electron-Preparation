#!/usr/bin/env python3
"""Six small checks for single-input leviton synthesis through a two-delay channel.

Use --output NEW.json. No old scientific code or reference is imported.
The analytic arbitrary-waveform statements are in SCOUT_08.md, not inferred
from the finite pulse or Fourier samples below.
"""
from __future__ import annotations
import argparse
from itertools import product
import json
from pathlib import Path
import unittest
import numpy as np
from scipy.integrate import quad
import sympy as sp

REPORT:dict[str,object]={}

def lorentz(t,w=1.,center=0.):
    if w<=0: raise ValueError('Width must be positive.')
    return 2*w/((np.asarray(t)-center)**2+w*w)

def phase(t,w=1.,center=0.):
    x=np.asarray(t)-center
    return (x+1j*w)/(x-1j*w)

def transfer(omega,p=.5,tau=1.):
    if not 0<=p<=1 or tau<=0:raise ValueError('Use 0 <= p <= 1 and tau > 0.')
    z=np.exp(1j*np.asarray(omega)*tau)
    return p+(1-p)*z

def scattering(omega,p=.5,tau=1.):
    z=np.exp(1j*omega*tau);c=np.sqrt(p*(1-p))
    return np.array([[p+(1-p)*z,c*(1-z)],[c*(1-z),(1-p)+p*z]],complex)

def energy_ratio(delta,a):
    """Exact integral after regularizing narrow real-frequency transmission minima.
    delta=abs(2p-1)>0, a=2w/tau. Ratio of input and target voltage fluences.
    """
    if not 0<delta<=1 or a<=0:raise ValueError('Require 0 < delta <= 1 and a > 0.')
    integ,err=quad(lambda y:np.exp(-2*a*np.arctan(delta*np.tan(y))),
                   -np.pi/2,np.pi/2,epsabs=2e-12,epsrel=2e-12,limit=200)
    return a*integ/(delta*np.sinh(np.pi*a)),a*err/(delta*np.sinh(np.pi*a))

def quotient_coefficients(target):
    """Integer Laurent orbit shifted to start at index zero. Returns f=(1+z)q."""
    a=list(map(int,target))
    if not a or min(a)<0:raise ValueError('Nonnegative target multiplicities required.')
    q=[];last=0
    for m in a[:-1]:
        last=m-last;q.append(last)
    return q,a[-1]-last

class ReachabilityChecks(unittest.TestCase):
    def test_fermionic_minimal_pulse_kernel(self):
        t,s,w=sp.symbols('t s w',real=True)
        Bt=(t+sp.I*w)/(t-sp.I*w);Bsc=(s-sp.I*w)/(s+sp.I*w)
        excess=sp.I*(Bt*Bsc-1)/(2*sp.pi*(t-s))
        rankone=w/(sp.pi*(t-sp.I*w)*(s+sp.I*w))
        self.assertEqual(sp.cancel(excess-rankone),0)
        # Product phases telescope into a positive sum of one-electron kernels.
        sets=[[(0.,.5)],[(0.,.5),(3.,.5)],[(0.,.5),(0.,.5),(1.,.8),(1.,.8)]]
        rows=[];sample=np.array([-2.3,-.7,.2,1.6,4.1])
        for pulses in sets:
            def orbital(t,j):
                c,w=pulses[j];v=np.sqrt(w/np.pi)/(t-c-1j*w)
                for c0,w0 in pulses[:j]:v*=phase(t,w0,c0)
                return v
            overlap=np.zeros((len(pulses),len(pulses)),complex)
            for j in range(len(pulses)):
                for k in range(len(pulses)):
                    fn=lambda x:np.conj(orbital(x,j))*orbital(x,k)
                    overlap[j,k]=quad(lambda x:fn(x).real,-np.inf,np.inf,epsabs=2e-10,limit=200)[0]+1j*quad(lambda x:fn(x).imag,-np.inf,np.inf,epsabs=2e-10,limit=200)[0]
            self.assertLess(np.linalg.norm(overlap-np.eye(len(pulses))),2e-9)
            O=np.array([[orbital(x,j) for j in range(len(pulses))]for x in sample])
            G=O@O.conj().T
            self.assertGreaterEqual(np.linalg.eigvalsh(G).min(),-1e-13)
            S=np.array([np.prod([phase(x,w,c) for c,w in pulses])for x in sample])
            off=np.array([[1j*(S[i]*S[j].conj()-1)/(2*np.pi*(sample[i]-sample[j])) if i!=j else sum(lorentz(sample[i],w,c) for c,w in pulses)/(2*np.pi) for j in range(len(sample))]for i in range(len(sample))])
            self.assertLess(np.linalg.norm(off-G),2e-14)
            rows.append(dict(electron_count=len(pulses),orbital_orthogonality_error=float(np.linalg.norm(overlap-np.eye(len(pulses)))),kernel_error=float(np.linalg.norm(off-G))))
        REPORT['clean_target_kernel']=rows

    def test_two_channel_scattering_and_one_port_zero(self):
        rows=[]
        for p in (.1,.5,.7,.99):
            for omega in (0.,.3,np.pi,2*np.pi,5*np.pi):
                S=scattering(omega,p)
                self.assertLess(np.linalg.norm(S.conj().T@S-np.eye(2)),8e-16)
                self.assertLess(abs(S[0,0]-transfer(omega,p)),1e-15)
                self.assertAlmostEqual(abs(S[0,0])**2+abs(S[1,0])**2,1.,places=14)
                if p==.5 and omega in (np.pi,5*np.pi):self.assertLess(abs(S[0,0]),1e-15)
            self.assertLess(np.linalg.norm(scattering(0,p)-np.eye(2)),1e-15)
            rows.append(dict(mixing=p,minimum_modulus_bound=abs(2*p-1)))
        x,a=sp.symbols('x a',positive=True)
        lim=sp.limit((x-sp.pi)**2*sp.exp(-a*x)/sp.cos(x/2)**2,x,sp.pi)
        self.assertEqual(sp.simplify(lim-4*sp.exp(-sp.pi*a)),0)
        REPORT['spectral_obstruction']=dict(rows=rows,pole_coefficient='4*exp(-pi*a)>0',meaning='The exact single-Lorentzian inverse is not square-integrable at an equal-mixing transmission zero.')

    def test_integer_orbit_divisibility_and_complete_construction(self):
        checked=0;reachable=0
        for length in range(1,9):
            for m in product((0,1),repeat=length):
                if not any(m):continue
                q,remainder=quotient_coefficients(m)
                alt=sum((-1)**j*x for j,x in enumerate(m))
                self.assertEqual(remainder,(-1)**(length-1)*alt)
                if remainder==0:
                    self.assertEqual(sum(m)%2,0)
                    reachable+=1
                    conv=np.convolve([1,1],q) if q else np.array([0])
                    self.assertTrue(np.array_equal(conv,m))
                checked+=1
        # A nontrivial valid output: two electrons three delays apart. The input
        # has signed pulse areas (2,-2,2), not a clean positive input pulse.
        q,rem=quotient_coefficients([1,0,0,1]);self.assertEqual(q,[1,-1,1]);self.assertEqual(rem,0)
        t=np.linspace(-4,7,151);f=lorentz(t,.5)+lorentz(t,.5,3.)
        vin=lambda x:2*(lorentz(x,.5)-lorentz(x,.5,1)+lorentz(x,.5,2))
        err=float(np.max(abs((vin(t)+vin(t-1))/2-f)))
        self.assertLess(err,2e-15)
        # Even charge alone is not sufficient: unequal widths do not share an orbit.
        impossible=2*np.pi*(np.exp(-.4*np.pi)+np.exp(-.8*np.pi)*np.exp(1j*np.pi))
        self.assertGreater(abs(impossible),.1)
        REPORT['finite_target_classification_checks']=dict(multiplicity_patterns=checked,reachable_patterns=reachable,all_reachable_counts_even=True,signed_input_weights=[2,-2,2],output_weights=[1,0,0,1],construction_error=err,even_unequal_width_target_has_nonzero_zero_frequency_amplitude=abs(impossible))

    def test_vandermonde_grouping_does_not_mix_distinct_orbits(self):
        # Illustration of the analytic all-size grouping proof. Distinct width/
        # center-modulo-delay pairs yield distinct bases for a finite exponential sum.
        groups=[(.4,0.),(.8,0.),(.4,.3),(.4,.7)]
        lam=np.array([np.exp(-2*np.pi*w+2j*np.pi*r)for w,r in groups])
        V=np.array([[z**k for z in lam]for k in range(len(lam))])
        det=np.linalg.det(V);formula=np.prod([lam[j]-lam[i]for i in range(len(lam))for j in range(i+1,len(lam))])
        self.assertGreater(abs(formula),1e-10)
        self.assertLess(abs(det-formula),1e-18)
        # Each group has vanishing alternating integer weight, independent of width.
        records=[(.4,0.,[1,0,0,1]),(.8,.3,[2,2]),(.6,.2,[1,2,1])]
        zero_vals=[]
        for k in range(8):
            omega=(2*k+1)*np.pi
            amp=sum(2*np.pi*np.exp(-w*omega+1j*r*omega)*sum(n*np.exp(1j*j*omega)for j,n in enumerate(m)) for w,r,m in records)
            self.assertLess(abs(amp),2e-14);zero_vals.append(float(abs(amp)))
        REPORT['orbit_grouping']=dict(vandermonde_determinant_modulus=float(abs(det)),target_zero_residuals=zero_vals,meaning='Finite examples only; Vandermonde linear independence proves the arbitrary finite number of groups analytically.')

    def test_inverse_energy_and_fixed_width_divergence(self):
        rows=[]
        for a in (.2,1.,2.):
            self.assertAlmostEqual(energy_ratio(1.,a)[0],1.,places=11)
            coefficient=np.pi*a/np.sinh(np.pi*a)
            scaled=[]
            for delta in (.1,.01,.001):
                R,err=energy_ratio(delta,a)
                self.assertGreaterEqual(R,1.-1e-10)
                self.assertLessEqual(R,1/delta**2+1e-9)
                scaled.append(delta*R/coefficient)
                rows.append(dict(a=a,imbalance=delta,energy_ratio=R,quadrature_error=err,scaled_to_asymptotic=scaled[-1]))
            self.assertLess(abs(scaled[-1]-1),abs(scaled[-2]-1))
            self.assertLess(abs(scaled[-2]-1),abs(scaled[-3]-1))
            self.assertLess(abs(scaled[-1]-1),.055)
        # Independent time-domain Lorentzian autocorrelation of the geometric inverse.
        # Integral of L_w(t)L_w(t-n*tau) divided by integral L_w^2 is a^2/(a^2+n^2).
        separate=[]
        for p,N in ((.7,90),(.55,250),(.51,900)):
            a=1.;r=(1-p)/p;co=(-r)**np.arange(N+1)/p
            difference=np.arange(N+1)[:,None]-np.arange(N+1)[None,:]
            value=float(co@(a*a/(a*a+difference*difference))@co)
            exact,_=energy_ratio(abs(2*p-1),a)
            self.assertLess(abs(value-exact),2e-10)
            separate.append(dict(mixing=p,terms=N+1,time_overlap_energy_ratio=value,spectral_energy_ratio=exact))
        z,r=sp.symbols('z r')
        for N in range(7):
            self.assertEqual(sp.expand((1+r*z)*sum((-r*z)**j for j in range(N+1))-(1-(-r*z)**(N+1))),0)
        REPORT['finite_energy_inverse']=dict(integral_rows=rows,independent_overlap=separate,asymptotic='E_in/E_target ~ [pi*a/sinh(pi*a)]/abs(2p-1), a=2w/tau fixed',boundary='This is exact-target source energy, not a finite-error electron-fidelity or hole-number bound.')

    def test_two_input_recovery_and_delayed_companion_control(self):
        t=np.linspace(-5,6,151);f=lambda x:lorentz(x,.5)
        v1=lambda x:(f(x)+f(x+1))/2
        v2=lambda x:(f(x)-f(x+1))/2
        out1=(v1(t)+v1(t-1)+v2(t)-v2(t-1))/2
        out2=(v1(t)-v1(t-1)+v2(t)+v2(t-1))/2
        self.assertLess(float(np.max(abs(out1-f(t)))),1e-15)
        self.assertLess(float(np.max(abs(out2))),1e-15)
        Ein=quad(lambda x:v1(x)**2+v2(x)**2,-np.inf,np.inf,epsabs=1e-10)[0]
        Eout=quad(lambda x:f(x)**2,-np.inf,np.inf,epsabs=1e-10)[0]
        self.assertLess(abs(Ein-Eout),2e-10)
        # A finite alternating train can place a clean extra electron outside an
        # observation window; it cannot produce a globally single clean electron.
        rows=[]
        for N in (0,1,2,3,6):
            vin=lambda x:2*sum((-1)**j*f(x-j)for j in range(N+1))
            expected=f(t)-(-1)**(N+1)*f(t-(N+1))
            err=float(np.max(abs((vin(t)+vin(t-1))/2-expected)))
            self.assertLess(err,4e-15)
            charge=1-(-1)**(N+1)
            self.assertIn(charge,(0,2))
            rows.append(dict(last_input_index=N,net_output_charge_in_e=charge,companion_delay=N+1,error=err))
        REPORT['scope_controls']=dict(two_port_output_errors=[float(np.max(abs(out1-f(t)))),float(np.max(abs(out2)))],total_two_port_fluence=Ein,target_fluence=Eout,finite_train_rows=rows,interpretation='One-driven-input restriction is essential. Counting only an early time window can hide the later electron or hole; no Cooper-pair or parity-conservation claim is made.')


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.output and args.output.exists():parser.error(f'Refusing existing output {args.output}')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ReachabilityChecks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',tests_run=result.testsRun,scope='Exact algebra and small waveform/Fourier checks. No independent proof review, many-body simulation, apparatus certificate, or exhaustive priority.')
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        with args.output.open('x',encoding='utf-8') as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)

if __name__=='__main__':main()
