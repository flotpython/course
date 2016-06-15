#!/usr/bin/env python

# re-ecriture et adaptation libre de http://xkcd.com/519/

import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot as plt
#import numpy as np

plt.xkcd()

dpi=100
# target size
x,y= 324, 201
# however we build something larger
fact=3
fig = plt.figure(dpi=dpi,figsize=(fact*float(x)/dpi,fact*float(y)/dpi))

fig.subplots_adjust(left=0.02,right=0.78,bottom=0.18,top=0.7)

fig.text(0.86,0.39,"impact\nsur\ncarriere",ha='center', fontsize=36)

fig.text(0.35,0.55,"Un MOOC\nPython ?", fontsize=60, ha='center',va='center')

#fig.text(0.01,0.01,"adaptation libre de http://xkcd.com/519/",
#         fontsize=14,ha='left',va='bottom')

ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.set_xlim([-0.5, 2.5])
ax.set_ylim([0, 110])
ax.bar([i-0.125 for i in range(3)], [4, 12, 100], 0.25)

ax.xaxis.set_ticks_position('bottom')
ax.tick_params(size=0)
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(["900 h\nde cours", 
                    "un livre\nsur python", 
                    "jouer avec\npython"])
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(28) 
plt.yticks([])
#ax.set_ylabel("impact\nsur\ncarriere", rotation='horizontal',
#              labelpad=80, va='center', fontsize=26)


fig.savefig('xkcd2.png')
fig.savefig('xkcd2-320x200.png')

plt.show()
