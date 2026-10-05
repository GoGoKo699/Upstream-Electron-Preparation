#!/usr/bin/env python3
"""Five bounded checks of the existing energy-optimal electron-preparation pulse.

Run: python check_control_audit.py --output NEW.json
These check calibration and energy-weighted duration of the SAME optimizer;
they do not solve a general robust, causal, or time-limited control problem.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import unittest
import numpy as np
from scipy.integrate import quad
import sympy as sp

from probe_calibration import sensitivity, residues, frontier, at_fidelity

REPORT:dict[str,object]={}


class ControlAuditChecks(unittest.TestCase):
    def test_exact_mismatch_identity_and_lorentzian_time_convention(self):
        c,s,mu,x,f,eps=sp.symbols('c s mu x f eps',real=True)
        d=c*c+mu*x
        # Remove the common phase e^{ix/2}. Then H0=c, G=-2i s.
        A=c*f/d
        residual=c*A-f
        perturbation=-2*sp.I*s*A
        lhs=sp.expand_complex((residual+eps*perturbation)*sp.conjugate(residual+eps*perturbation))
        self.assertEqual(sp.factor(lhs-residual**2-4*eps**2*s**2*c**2*f**2/d**2),0)
        self.assertEqual(sp.simplify(sp.re(residual*sp.conjugate(perturbation))),0)
        # Convention: A(x)=e^{-ix/2}b(x); Fourier sign is exp(+i omega t).
        b,bp=sp.symbols('b bp',real=True)
        derivative=-sp.I*b/2+bp
        self.assertEqual(sp.simplify(sp.re(-sp.I*b*derivative)+b*b/2),0)
        self.assertEqual(sp.expand_complex(derivative*sp.conjugate(derivative))-b*b/4-bp*bp,0)
        checks=[]
        for width in (.25,.7,2.):
            en=quad(lambda t:(2*width/(t*t+width*width))**2,-np.inf,np.inf,epsabs=1e-11)[0]
            m2=quad(lambda t:t*t*(2*width/(t*t+width*width))**2,-np.inf,np.inf,epsabs=1e-11)[0]
            self.assertLess(abs(m2/en-width*width),2e-11)
            spectral_u=1/(2*width)
            spectral_v=width/2
            self.assertLess(abs(m2/en-spectral_v/spectral_u),2e-11)
            checks.append(dict(width=width,time_second_moment=m2/en,Parseval_second_moment=spectral_v/spectral_u))
        REPORT['algebra_and_duration_convention']={'exact_cross_term':0,'mean_source_time_over_tau':'-1/2','lorentzian_controls':checks}

    def test_independent_actual_output_mismatch_integral(self):
        rows=[]
        for mu,a in ((.003,.25),(.0002,.5),(.01,1.)):
            nominal=frontier(mu,a);extra=sensitivity(mu,a)
            cutoff=extra['cutoff']
            # Independent direct x coordinate, subdivided at nodes for moderate mu.
            nodes=np.arange(np.pi,cutoff,np.pi)
            for eps in (-.02,-.001,.001,.02):
                def integrand(x):
                    if x==0:return 0.
                    H0=(1+np.exp(1j*x))/2
                    Hactual=.5+eps+(.5-eps)*np.exp(1j*x)
                    f=np.exp(-a*x/2)
                    A=H0.conjugate()*f/(abs(H0)**2+mu*x)
                    return abs(Hactual*A-f)**2/x
                actual=quad(integrand,0,cutoff,points=nodes,epsabs=3e-11,epsrel=3e-11,limit=2000)[0]
                prediction=nominal['infidelity_exponent']+eps*eps*extra['K']
                self.assertLess(abs(actual-prediction),3e-10)
                rows.append(dict(mu=mu,a=a,actual_p=.5+eps,direct_D=actual,identity_D=prediction,difference=abs(actual-prediction)))
        REPORT['independent_mismatch_checks']=rows

    def test_derivative_quadrature_and_infinite_tail_controls(self):
        rows=[]
        for mu,a in ((.003,.25),(.001,.5),(.01,1.)):
            extra=sensitivity(mu,a)
            cutoff=extra['cutoff']
            def dx(x):
                c=np.cos(x/2);cp=-np.sin(x/2)/2;d=c*c+mu*x
                return np.exp(-a*x/2)*((cp-a*c/2)/d-c*(-np.sin(x)/2+mu)/d**2)
            direct=quad(lambda x:dx(x)**2,0,cutoff,points=np.arange(np.pi,cutoff,np.pi),epsabs=2e-9,epsrel=2e-10,limit=2000)[0]
            den=frontier(mu,a)['energy_ratio']/a
            expected=extra['centered_time_second_moment_ratio']*den
            self.assertLess(abs(direct/expected-1),3e-9)
            # Numerical derivatives are an independent local check, not used in the main quadrature.
            derivative_errors=[]
            for x in (.1,1.,2.7,3.1,3.2,4.,8.):
                h=2e-6
                fun=lambda y:np.cos(y/2)*np.exp(-a*y/2)/(np.cos(y/2)**2+mu*y)
                approx=(fun(x-2*h)-8*fun(x-h)+8*fun(x+h)-fun(x+2*h))/(12*h)
                derivative_errors.append(abs(approx-dx(x))/max(1.,abs(dx(x))))
            self.assertLess(max(derivative_errors),5e-9)
            self.assertLess(extra['K_tail_bound'],1e-18)
            self.assertLess(extra['derivative_tail_bound'],1e-16)
            rows.append(dict(mu=mu,a=a,direct_derivative_norm=direct,geometric_derivative_norm=expected,max_local_derivative_error=max(derivative_errors),K_tail_bound=extra['K_tail_bound'],derivative_tail_bound=extra['derivative_tail_bound']))
        REPORT['duration_and_tail_checks']=rows

    def test_asymptotic_constants_not_fitted(self):
        z=sp.symbols('z',real=True)
        integral=sp.integrate((1-z*z)**2/(1+z*z)**4,(z,-sp.oo,sp.oo))
        self.assertEqual(sp.simplify(integral-sp.pi/4),0)
        rows=[]
        for a in (.25,.5,1.):
            for mu in (1e-5,1e-7,1e-9):
                d=sensitivity(mu,a)
                ratios=dict(K=d['scaled_K']/d['asymptotic_scaled_K'],derivative_norm=d['scaled_derivative_norm']/d['asymptotic_scaled_derivative'],D_K=d['D_times_K']/d['limit_D_times_K'],D_duration=d['D_times_duration']/d['limit_D_times_duration'])
                if mu==1e-9:
                    self.assertTrue(all(abs(v-1)<.002 for v in ratios.values()),ratios)
                self.assertTrue(all(v>0 for v in ratios.values()))
                rows.append(dict(a=a,mu=mu,ratios=ratios))
        REPORT['asymptotic_checks']={'universal_integral':'pi/4','samples':rows,'proof_scope':'Limits derived from isolated transmission zeros in SCOUT_10.md; not inferred from these samples.'}

    def test_finite_fidelity_calibration_and_duration_table(self):
        rows=[]
        for a in (.25,.5,1.,2.):
            target=at_fidelity(.999,a);mu=target['mu'];D=target['infidelity_exponent']
            values=sensitivity(mu,a)
            refined=sensitivity(mu,a,4e-11)
            self.assertLess(abs(values['K']/refined['K']-1),2e-9)
            self.assertLess(abs(values['rms_energy_duration_over_tau']/refined['rms_energy_duration_over_tau']-1),2e-9)
            eps_limit=np.sqrt(.1*D/values['K'])
            actualF=np.exp(-D-1e-6*values['K'])
            self.assertLess(actualF,.999)
            self.assertLess(abs(np.exp(-D-eps_limit**2*values['K'])-.999**1.1),2e-13)
            self.assertGreater(eps_limit,0.)
            rows.append(dict(a=a,target_width_over_tau=a/2,nominal_fidelity=.999,mu=mu,energy_ratio=target['energy_ratio'],rms_energy_duration_over_tau=values['rms_energy_duration_over_tau'],K=values['K'],p_offset_for_10percent_extra_log_infidelity=eps_limit,fidelity_at_p_offset_0_001=actualF,source_mean_time_over_tau=-.5))
        # Same fixed calibration offset can make further ideal optimization harmful.
        d1=frontier(1e-7,.25)['infidelity_exponent']+1e-6*sensitivity(1e-7,.25)['K']
        d2=frontier(1e-11,.25)['infidelity_exponent']+1e-6*sensitivity(1e-11,.25)['K']
        self.assertGreater(d2,d1)
        REPORT['finite_target_table']=rows
        REPORT['overcompensation_control']={'fixed_a':.25,'fixed_p_error':.001,'mu_first':1e-7,'mu_more_ideal':1e-11,'actual_D_first':d1,'actual_D_more_ideal':d2,'scope':'Fixed nominal symmetric optimizer, not the known-asymmetric or minimax-robust optimum.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.output and args.output.exists():parser.error(f'Refusing existing output {args.output}')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ControlAuditChecks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',tests_run=result.testsRun,
                  scope='Analytic same-model diagnostics and refined 1D quadrature, not microscopic device performance, a general robustness bound, or a novelty certificate.')
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        with args.output.open('x',encoding='utf-8') as out:json.dump(REPORT,out,indent=2,sort_keys=True,allow_nan=False);out.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)

if __name__=='__main__':main()
