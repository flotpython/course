#!/usr/bin/env python

import random

import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot as plt
#import numpy as np

plt.xkcd()

import this
print '========================================'
def decode_c (c): return this.d[c] if c in this.d else c
def decode_l (l): return ''.join( [ decode_c(c) for c in l ])
original_aphorisms = [ decode_l(l) for l in this.s.split('\n') if l ]    
original_n = len(original_aphorisms)

####################
dpi=100
# target size
x,y= 1250, 354
# however we build something larger
fact=1
fig = plt.figure(dpi=dpi,figsize=(fact*float(x)/dpi,fact*float(y)/dpi))

def draw (layout,strings):
    for text,(x,y,angle,fontsize,color,ha,va) in zip (strings,layout):
        fig.text (x,y,text,rotation=angle,fontsize=fontsize,color=color,ha=ha,va=va)

FONT_SMALL,FONT_LARGE=14,32
X_left=0.05
X_right=0.84
Y_bottom=0.05

ANGLE=45

# on ne prend que les plus courts; on enleve celui qui tombe a plat
title=original_aphorisms[0]
title=["The zen of\nPython","by tim peters"]
aphorisms = [ a.strip('.') for a in original_aphorisms[1:] if len(a)<=40 and 'Although' not in a ]
aphorisms.append ('......')
n=len(aphorisms)

delta=float(X_right-X_left)/(n-1)
layout_title = [ (.11,0.68,0,FONT_LARGE,'k','center','center'), 
                 (.11,.5,0,10,'k','center','center'),
]
layout_aphos = [ (X_left+i*delta,Y_bottom, ANGLE, FONT_SMALL, 'b','left','bottom')
                 for i,a in zip(range(n),aphorisms) ]
layout = layout_aphos + layout_title
items = aphorisms + title
# Le titre vient en premier

draw (layout,items)

fig.savefig('xkcd3.png')

plt.show()

### random but reproducible
#random.seed(0)
##
#X_MIN,X_MAX = 0,1.
#Y_MIN,Y_MAX = 0.2,0.8
#ANGLE_MIN,ANGLE_MAX = -60,60
#X = [ random.uniform(X_MIN,X_MAX) for a in aphorisms ]
#Y = [ random.uniform(Y_MIN,Y_MAX) for a in aphorisms ]
#angles = [ random.uniform(ANGLE_MIN,ANGLE_MAX) for a in aphorisms ]
#font_sizes = [ int (random.uniform(FONT_MIN,FONT_MAX)) for a in aphorisms ]
#for i,a,x,y,angle,size in zip (range(n),aphorisms,X,Y,angles,font_sizes):
#    pass
##    fig.text (x,y,"%s:%s"%(i,a),rotation=angle,fontsize=size,ha='center',va='center')
#

#
#layout = [
#    (0.5,0.9,0,1.,'k','center','center'),
#    (0.2,0.4,45,.8,'r','center','center'),
#    (0.225,0.545,-45,.6,'b','center','center'),
#    (.5,.5,0,.6,'g','center','center'),
##    (.5,.5,0,.6,'g')
#]

