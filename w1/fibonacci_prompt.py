#!/usr/bin/env python
# -*- coding: utf-8

def fibonacci (n):
    if n <= 1 : 
        return 1
    f2, f1 = 1, 1
    for i in range (2,n+1):
        f2, f1 = f1, f1+f2
#        print i, f2, f1
    return f1

entier = int ( raw_input ("Entrer un entier "))
print "fibonacci({}) = {}".format(entier, fibonacci (entier))
