from colour import *
import numpy as np
from PIL import Image
NEW={'mol-semaglutide':'#496ba8','mol-gprotein':'#946ea0','mol-exendin4':'#9b6849','mol-albumin':'#a17c3b','mol-pi3k-p110':'#935573',
 'extra-ground':'#f3bfbd','extra-tile':'#ebb0ad','extra-line':'#c58484','bilayer-head':'#d5ab6b','bilayer-line':'#9a723e',
 'nucleus':'#6b4b80','cell-wall':'#7f5e84'}
def derived(fill):
    line=shade(fill,.55); light=mix(fill,T['mol-light'],.28); sh=mix(mix(fill,line,.32),T['mol-shadow-tint'],.10)
    return [fill,line,light,sh]
def pairs(keys):
    P=[]
    for k in keys:
        o,n=T[k],NEW[k]
        if k.startswith('mol-'): P+=list(zip(derived(o),derived(n)))
        else: P.append((o,n))
    return P
def rgb(h):return np.array([int(h[i:i+2],16) for i in (1,3,5)],float)
def recolor(src,dst,keys,keep=[],thr=22):
    im=np.asarray(Image.open(src).convert('RGB')).astype(float)
    P=pairs(keys)+[(T[k],T[k]) for k in keep]
    O=np.stack([rgb(o) for o,n in P]);D=np.stack([rgb(n)-rgb(o) for o,n in P])
    d=((im[:,:,None,:]-O[None,None])**2).sum(-1)**.5
    i=d.argmin(-1);m=d.min(-1)
    w=np.clip(1-(m-thr*.5)/(thr*.5),0,1)[...,None]
    out=im+D[i]*w
    Image.fromarray(np.clip(out,0,255).astype('uint8')).save(dst)
