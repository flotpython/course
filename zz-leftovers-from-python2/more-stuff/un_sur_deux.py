#!/usr/bin/env python

input1 = ( [ 1,2,3,5,8,13],
           [ 'a','b','c','e','h','m'] )

input2 = ( range(1,5), range (101,105) )

inputs = [ input1, input2 ]

# Oh!
def un_sur_deux (l1,l2):
    result = []
    for i in range(len(l1)):
        result.append(l1[i])
        result.append(l2[i])
    return result

####################
def test_function (function_to_test):
    fun_name=function_to_test.__name__
    print 20*"=","Test avec",fun_name
    for l1,l2 in inputs:
        print 10*"="
        print "l1",l1
        print "l2",l2
        # on appelle list pour voir les iterateurs
        print fun_name,"=>",list(function_to_test (l1,l2))

test_function (un_sur_deux)
