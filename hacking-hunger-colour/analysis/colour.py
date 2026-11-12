import json,math
def hx(h):h=h.lstrip('#');return tuple(int(h[i:i+2],16)/255 for i in (0,2,4))
def lin(c):return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def delin(c):c=max(0,min(1,c));return 12.92*c if c<=0.0031308 else 1.055*c**(1/2.4)-0.055
def L(h):r,g,b=map(lin,hx(h));return 0.2126*r+0.7152*g+0.0722*b
def cr(a,b):la,lb=sorted([L(a),L(b)]);return (lb+0.05)/(la+0.05)
def oklab_lin(r,g,b):
    l=0.4122214708*r+0.5363325363*g+0.0514459929*b
    m=0.2119034982*r+0.6806995451*g+0.1073969566*b
    s=0.0883024619*r+0.2817188376*g+0.6299787005*b
    l,m,s=[x**(1/3) if x>0 else 0 for x in (l,m,s)]
    return (0.2104542553*l+0.7936177850*m-0.0040720468*s,1.9779984951*l-2.4285922050*m+0.4505937099*s,0.0259040371*l+0.7827717662*m-0.8086757660*s)
def oklab(h):return oklab_lin(*map(lin,hx(h)))
def oklch(h):
    l,a,b=oklab(h);return (l,math.hypot(a,b),(math.degrees(math.atan2(b,a))%360))
def dE(a,b):
    A,B=oklab(a),oklab(b);return 100*math.dist(A,B)
# Machado 2009 severity 1.0
M={'prot':[[0.152286,1.052583,-0.204868],[0.114503,0.786281,0.099216],[-0.003882,-0.048116,1.051998]],
   'deut':[[0.367322,0.860646,-0.227968],[0.280085,0.672501,0.047413],[-0.011820,0.042940,0.968881]],
   'trit':[[1.255528,-0.076749,-0.178779],[-0.078411,0.930809,0.147602],[0.004733,0.691367,0.303900]]}
def sim(h,k):
    v=list(map(lin,hx(h)));m=M[k];o=[sum(m[i][j]*v[j] for j in range(3)) for i in range(3)]
    return '#'+''.join('%02x'%round(delin(x)*255) for x in o)
def dEcvd(a,b):return min(dE(sim(a,k),sim(b,k)) for k in M), {k:round(dE(sim(a,k),sim(b,k)),1) for k in M}
def mix(a,b,t):
    A,B=hx(a),hx(b);return '#'+''.join('%02x'%round((A[i]*(1-t)+B[i]*t)*255) for i in range(3))
def shade(a,f):return '#'+''.join('%02x'%round(x*f*255) for x in hx(a))
def lch2hex(l,c,h):
    a,b=c*math.cos(math.radians(h)),c*math.sin(math.radians(h))
    l_=l+0.3963377774*a+0.2158037573*b; m_=l-0.1055613458*a-0.0638541728*b; s_=l-0.0894841775*a-1.2914855480*b
    l3,m3,s3=l_**3,m_**3,s_**3
    r=4.0767416621*l3-3.3077115913*m3+0.2309699292*s3
    g=-1.2684380046*l3+2.6097574011*m3-0.3413193965*s3
    b_=-0.0041960863*l3-0.7034186147*m3+1.7076147010*s3
    return '#'+''.join('%02x'%round(delin(x)*255) for x in (r,g,b_))
import os
T={t['name']:t['value'] for t in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'tokens-v13.json')))['color']['tokens']}
