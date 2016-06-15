import matplotlib.pyplot as plt
import numpy as np

from matplotlib.pylab import cm

def display ( tuples_list ):
    size=len(tuples_list)
    image = np.zeros(size*size)
    for tuple in tuples_list:
        x,y=tuple
        image [ size*(x-1) + (y-1) ] = 1.
    # Reshape things into a 9x9 grid.
    image = image.reshape((size,size))
    row_labels = range(size)
    col_labels = [ chr (65+x) for x in xrange (size) ]
    plt.matshow(image, cmap=cm.gray)
    plt.xticks(range(size), col_labels)
    plt.yticks(range(size), row_labels)
    plt.show()
