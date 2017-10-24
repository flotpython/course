#!/usr/bin/env python3

# re-writing a free adaptation of http://xkcd.com/519/

import matplotlib
# this is what I need to do on my mac
# but it is not needed within a notebook
# matplotlib.use('TkAgg')

from matplotlib import pyplot as plt

# the magical trick to get friendly pictures
# that remind of the xkcd style
plt.xkcd()

# create figure
my_dpi = 80
fig = plt.figure(dpi=my_dpi, figsize=(9, 6))

# we need more space for the labels and all
fig.subplots_adjust(left=0.25, bottom=0.22, top=0.65)

# do not use title, we draw our own texts
fig.text(0.01, 0.01, "adaptation libre de http://xkcd.com/519/",
         fontsize=14, ha='left', va='bottom')

# another text
fig.text(0.5, 0.82,
         """Python:
des fondamentaux
a l'utilisation du langage""",
         fontsize=45, ha='center', va='center')

# a subplot
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# set scales
ax.set_xlim([-0.5, 2.5])
ax.set_ylim([0, 110])
# set values
ax.bar([i - 0.125 for i in range(3)], [5, 3, 100], 0.25)

# draw labels for x and y
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(size=0)
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(["900\nHEURES\nDE COURS",
                    "400\nHEURES\nDE DM",
                    "UN MOOC\nA JOUER\nAVEC PYTHON"])
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(26)

plt.yticks([])
ax.set_ylabel(
    """utilite
pour une
carriere
reussie""",
    rotation='horizontal',
    labelpad=80,
    va='center',
    fontsize=26)

# show it
plt.show()
