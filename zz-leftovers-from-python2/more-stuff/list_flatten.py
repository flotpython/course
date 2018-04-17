#!/usr/bin/env python

input1= [ 'a', 'b', 'c' ]
# works with an iterator as well
input2 = xrange(4)
# a random tree
input3 = [ 1, 2, [3, [4, [5, 6] ,7] ,8], 9]
# generating lists
input4 = [ [ n**2, n**2+1 ] for n in range (1,6) ]
# a list of turtle moves
input5 = [ [ ('forward', 100,), ('left', 120,) ] for i in xrange(3) ]
# 2-depth tree
input6 = [ [ [ 0, 1 ] for j in xrange(3) ] for i in xrange (3) ]

inputs = [ input1, input2, input3, input4, input5, input6 ]

def list_flatten (list_of_lists):
    result=[]
    for l in list_of_lists:
        if isinstance (l,list):
            result += list_flatten (l)
        else:
            result.append(l)
    return result

def main ():
    for input in inputs:
        margin = len('flattened')-len('input')-1
        print margin*'=','input:', input
        print 'flattened:', list_flatten (input)

if __name__ == '__main__': main()
