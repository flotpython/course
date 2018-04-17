#!/usr/bin/env python

from operator import add

from math import factorial

def count_couples (n):
    return n+1

# enumerate all couples of integers >=0 so that their sum is n
def enumerate_couples (n):
    return [ (i,n-i) for i in xrange(n+1)]

# enumrate all triples of integers >=0 so that their sum is n
def enumerate_triples (n):
    # xxx should return an iterator
    result = []
    for i in xrange(n+1):
        for (j,k) in enumerate_couples(n-i):
            result.append ( (i,j,k) )
    return result

def count_triples (n):
    return reduce (add, [ count_couples(i) for i in xrange(n+1)])

def count_ternaries (n):
    # initialize the number of ternaries starting with 0 and upwards
    number_ternaries=[0 for i in xrange(n+1)]
    # to compute at level m, since we already have the root
    # we iterate on all triples (i,j,k) that sum to m-1
    # for each triple we have Ti * Tj * Tk trees to count
    for m in xrange(n+1):
        # there is one ternary with 0 node
        if m==0:
            number_ternaries[m]=1
        else:
            for (i,j,k) in enumerate_triples(m-1):
                number_ternaries[m] += number_ternaries[i]*number_ternaries[j]*number_ternaries[k]
        res_m=number_ternaries[m]
        direct=direct_count(m)
        nb_skews=(2*res_m)/(m+1)
        check1= res_m==direct
        check2= (2*res_m)%(m+1)==0
        check = "OK" if check1 and check2 else "KO"
        if m%10==0: print "number_ternaries[%s]=%s (skews=%s check %s)"%\
           (m,res_m,nb_skews,check)
    return number_ternaries[n]

def print_list (l,max):
    counter=0
    for x in l: 
        print x
        counter+=1
        if counter>=max: 
            print '...'
            return

# an experimentally conjectured count
# probably easy to show by inference
def direct_count (n):
    return factorial(3*n)/(factorial(2*n)*factorial(n)*(2*n+1))

debug=True
#debug_samples=[0,1,2,3,5,8,10]
debug_samples=[0,1,2,3]
debug_max = 20


def main ():
    from argparse import ArgumentParser
    parser=ArgumentParser()
    parser.add_argument("n",type=int,help="number of nodes in the ternary")
    parser.add_argument("-d","--debug",dest='debug',action='store_true',default=False,help="set to debug")
    args=parser.parse_args()
    n=args.n
    if args.debug:
        debug_samples=xrange(n+1)
        for n in debug_samples: 
            couples=enumerate_couples(n)
            print "========== %s  - check %s - couples that sum to %s"%(len(couples),count_couples(n),n)
            print_list (couples,debug_max)
        for n in debug_samples: 
            triples = enumerate_triples(n)
            print "========== %s - check %s - triples that sum to %s"%(len(triples),count_triples(n),n)
            print_list (triples, debug_max)
    ternaries = count_ternaries (args.n)
    print "%s ternaries with %s nodes"%(ternaries,n)


if __name__ == '__main__':
    main()
