#!/usr/bin/env python

# re-ecriture et adaptation libre de http://xkcd.com/519/

import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot as plt
import numpy as np

plt.xkcd()

my_dpi=80
fig = plt.figure(dpi=my_dpi,figsize=(9,6))

fig.subplots_adjust(left=0.25,bottom=0.22,top=0.65)

fig.text(0.01,0.01,"adaptation libre de http://xkcd.com/519/",
         fontsize=14,ha='left',va='bottom')

fig.text(0.5,0.82,"Python:\ndes fondamentaux\na l'utilisation du langage",
         fontsize=45, ha='center',va='center')

#plt.title("Python\ndes fondements\naux applications",fontsize=45)

ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.set_xlim([-0.5, 2.5])
ax.set_ylim([0, 110])
ax.bar([i-0.125 for i in range(3)], [5, 3, 100], 0.25)

ax.xaxis.set_ticks_position('bottom')
ax.tick_params(size=0)
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(["900\nHEURES\nDE COURS", 
                    "400\nHEURES\nDE DM", 
                    "UN MOOC\nA JOUER\nAVEC PYTHON"])
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(26) 
plt.yticks([])
ax.set_ylabel("utilite\npour une\ncarriere\nreussie",
              rotation='horizontal',
              labelpad=80,
              va='center',
              fontsize=26)


fig.savefig('xkcd.png')

## the pictures I can see on FUN are 220 x 147
# the wet finger technique...
# this does produce a 220x147 output but the fonts are not resized accordingly...
# so do this under preview & adjust size...
#h=1.47
#fig.set_size_inches (h*1.5,h)
#fig.savefig('xkcd-220x147.png')
fig.savefig('xkcd-220x147.png')

plt.show()
