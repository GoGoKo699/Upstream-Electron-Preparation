import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import jv
from math import pi

def coeff(a):
 k=np.arange(max(10,int(25/a)))
 x=(2*k+1)*pi
 B=pi*np.sum(np.exp(-a*x)/np.sqrt(x))
 return B,a*B*B

def frontier(mu,a,order_tol=2e-10):
 # Integrate half-cells about each transfer zero with tangent coordinates.
 # y=tan(theta), x=x_k+2 sqrt(mu x_k) tan(theta).
 n=max(2,int(np.ceil(34/(2*pi*a))))
 E=0.;D=0.
 for k in range(n):
  z=(2*k+1)*pi
  c=2*np.sqrt(mu*z)
  l=np.arctan(-pi/c); r=np.arctan(pi/c)
  def f(t,which):
   y=np.tan(t);x=z+c*y; dx=c*(1+y*y)
   if x<0 and x>-1e-10:x=0.
   h=np.cos(x/2)**2;den=h+mu*x
   return (h if which=='E' else mu*mu*x)*np.exp(-a*x)/den**2*dx
  E+=quad(lambda t:f(t,'E'),l,0,epsabs=order_tol,epsrel=order_tol,limit=120)[0]+quad(lambda t:f(t,'E'),0,r,epsabs=order_tol,epsrel=order_tol,limit=120)[0]
  D+=quad(lambda t:f(t,'D'),l,0,epsabs=order_tol,epsrel=order_tol,limit=120)[0]+quad(lambda t:f(t,'D'),0,r,epsabs=order_tol,epsrel=order_tol,limit=120)[0]
 return a*E,D

if __name__=='__main__':
 for A in (.2,1.,2.):
  m=np.arange(1,41)[:,None];q=np.arange(40)[None,:]
  B=(1j)**(-m-q)*jv(-m-q,A)
  hh=B@B.conj().T
  sign,lf=np.linalg.slogdet(np.eye(40)-hh)
  print('Bessel',A, 'F',np.exp(lf),'expected',np.exp(-A*A/4),'holes',np.trace(hh).real,'D',A*A/4)
 for a in (.25,.5,1.,2.):
  B,C=coeff(a);print('a',a,'B',B,'C',C)
  for F in (.99,.999,.9999):
   target=-np.log(F)
   lm=brentq(lambda z:frontier(np.exp(z),a)[1]-target,-30,10,xtol=1e-11)
   mu=np.exp(lm);R,D=frontier(mu,a)
   print(F,mu,R,D,'RD',R*D)
 for m in (1e-3,1e-5,1e-7,1e-9):
  R,D=frontier(m,1)
  print('asym',m,R,D,R*D)
