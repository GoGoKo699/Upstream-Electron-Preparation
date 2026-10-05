"""Pole-resolved calibration and time-moment integrals for the fixed optimizer.

Functions return quadrature estimates with separate analytic frequency-tail bounds.
No discretized transmission zero is interpreted as an exact finite-energy inverse.
"""
from pathlib import Path
import sys
from functools import lru_cache
import numpy as np
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'prior'))
from check_finite_accuracy import frontier,at_fidelity,residue_coefficient


def residues(a):
    n=max(12,int(np.ceil(45/(2*np.pi*a))))
    x=(2*np.arange(n)+1)*np.pi
    B0=float(np.pi*np.sum(np.exp(-a*x)/np.sqrt(x)))
    B1=float(np.pi*np.sum(np.exp(-a*x)/x**1.5))
    return B0,B1

@lru_cache(None)
def sensitivity(mu,a,tol=2e-10):
    if mu<=0 or a<=0:raise ValueError('Positive parameters required')
    count=max(2,int(np.ceil(max(65.,4*np.log(1/mu)+40)/(2*np.pi*a))))
    kval=derivative=err=0.
    for k in range(count):
        zero=(2*k+1)*np.pi
        cut=[0.,min(2*np.sqrt(mu*zero),np.pi)]
        while cut[-1]<np.pi:cut.append(min(2*cut[-1],np.pi))
        def fun(s,which):
            x=zero+s
            c=np.sin(s/2);cp=.5*np.cos(s/2)
            h=c*c;hp=c*np.cos(s/2);den=h+mu*x
            f=np.exp(-a*x/2)
            if which==0:
                return np.sqrt(mu)*4*h*(1-h)*f*f/(x*den*den)
            db=f*((cp-.5*a*c)/den-c*(hp+mu)/(den*den))
            return mu**1.5*db*db
        accum=[]
        for which in (0,1):
            z=0.
            for lo,hi in zip(cut[:-1],cut[1:]):
                for sign in (1,-1):
                    val,e=quad(lambda y:fun(sign*y,which),lo,hi,epsabs=tol,epsrel=tol,limit=100)
                    z+=val;err+=e
            accum.append(z)
        kval+=accum[0];derivative+=accum[1]
    cutoff=2*np.pi*count
    k=kval/np.sqrt(mu);num=derivative/mu**1.5
    old=frontier(mu,a)
    U=old['energy_ratio']/a
    B0,B1=residues(a)
    return dict(mu=mu,a=a,K=k,centered_time_second_moment_ratio=num/U,
                rms_energy_duration_over_tau=np.sqrt(num/U),scaled_K=kval,scaled_derivative_norm=derivative,
                asymptotic_scaled_K=4*B1,asymptotic_scaled_derivative=B1/8,
                D_times_K=old['infidelity_exponent']*k,limit_D_times_K=4*B0*B1,
                D_times_duration=old['infidelity_exponent']*np.sqrt(num/U),limit_D_times_duration=np.sqrt(B0*B1/8),
                quadrature_scaled_error_estimate=err,cutoff=cutoff,
                K_tail_bound=float(np.exp(-a*cutoff)/(a*mu*cutoff**2)),
                derivative_tail_bound=float(np.exp(-a*cutoff)/a*(2*((1+a)/(2*mu*cutoff))**2+2*((.5+mu)/(mu**2*cutoff**2))**2)))

