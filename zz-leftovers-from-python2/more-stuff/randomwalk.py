#!/usr/bin/env python

import random
from argparse import ArgumentParser

class RandomWalk:
    def __init__ (self, length, border):
        self.length=length
        self.border=border
        self.counter=0
        self.current=0
    def __iter__(self):
        return self
    def next(self):
        # are we done ?
        if self.counter==self.length:
            raise StopIteration
        # remember current position and compute next
        result=self.current
        self.counter += 1
        # compute sign of next move
        (bottom,top) = (-1,1)
        # if at the border.. 
        if self.current==self.border:           move=random.randint(-1,0)
        elif self.current== -self.border:       move=random.randint(0,1)
        else:                                   move=random.randint(-1,1)
        self.current += move
        return result

import matplotlib.pyplot as plt

def draw_walks (length, border, runs):
    print 'runs',runs
    for i in xrange(runs):
        random_walk = RandomWalk (length, border)
        data = [ y for y in random_walk ] 
        plt.plot ( data )
        plt.axis ( [ 0,length,-border,border] )
    plt.ylabel ( "%s random walk(s) %s x %s" % (runs, length, border))
    plt.show ()
        
def main ():
    parser = ArgumentParser (description="generate a randomwalk of length <length> and with absolute value constrained by <border>")
    parser.add_argument ("length", type=int)
    parser.add_argument ("border", type=int)
    parser.add_argument ("runs", type=int, default=1, nargs='?')
    args=parser.parse_args ()

    random.seed()

    draw_walks ( args.length, args.border, args.runs )

if __name__ == '__main__':
    main()
