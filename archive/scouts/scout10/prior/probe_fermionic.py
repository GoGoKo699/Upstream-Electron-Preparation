import numpy as np
from scipy.linalg import eigh
from check_finite_accuracy import frontier
from math import pi

def periodic(mu,a,step,cutoff):
 freq=step*np.arange(1,cutoff+1)
 h=np.cos(freq/2)**2
 error=-mu*freq*np.exp(-a*freq/2)/(h+mu*freq)
 phi_plus=1j*error/np.arange(1,cutoff+1)
 N=8192
 arr=np.zeros(N,complex);arr[1:cutoff+1]=phi_plus;arr[-cutoff:]=phi_plus[::-1].conj()
 phi=np.fft.fft(arr).real
 U=np.exp(-1j*phi);co=np.fft.ifft(U)
 m=np.arange(1,cutoff+1)[:,None];q=np.arange(cutoff)[None,:]
 X=co[(-m-q)%N];H=X@X.conj().T
 sign,lnF=np.linalg.slogdet(np.eye(cutoff)-H)
 D=sum(abs(error)**2/np.arange(1,cutoff+1))
 return dict(mu=mu,step=step,N=cutoff,F_det=float(np.exp(lnF)),F_boson=float(np.exp(-D)),D=D,Nh=float(np.trace(H).real),dmax=max(abs(phi)),fullD=frontier(mu,a)['infidelity_exponent'])
for step in (.2,.1):
 for n in (128,256):print(periodic(.05,1.,step,n))
