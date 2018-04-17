#!/usr/bin/env python

from operator import add

from math import factorial

class CouplesBySum:
    "an iterator that enumerates all couples of integers that sum to n"
    def __init__ (self,n):
        self.n = n
        self.counter = 0
    def __iter__ (self):
        return self
    def next(self):
        if self.counter > self.n:
            raise StopIteration
        else:
            result=(self.counter, self.n - self.counter)
            self.counter += 1
            return result
    def __len__(self):
        return self.n+1


class TriplesBySum:
    "an iterator that enumerates all triples of integers that sum to n"
    def __init__ (self,n):
        self.n=n
        self.counter1 = 0
        self.counter2 = 0
    def __iter__(self): 
        return self
    def next(self):
        if self.counter1>self.n: 
            raise StopIteration
        elif self.counter2+self.counter1>=self.n:
            result = (self.counter1, self.counter2, self.n - self.counter1 - self.counter2)
            self.counter1 += 1
            self.counter2 = 0
        else:
            result = (self.counter1, self.counter2, self.n - self.counter1 - self.counter2)
            self.counter2 += 1
        return result
    def __len__ (self):
        "number of triples : (n+1)+n+(n-1)+...+1 = (n+2)(n+1)/2"
        return ((self.n+2)*(self.n+1))/2

def enumerate_triples(n):
    return TriplesBySum(n)

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
    count_ternaries (args.n)


if __name__ == '__main__':
    main()
