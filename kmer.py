#! /usr/bin/python3m

import sys

n=int(sys.argv[1])

l1=['A','T','G','C']
l2=['A','T','G','C']


def mer(l1,l2,n):
    if n==1:
        return l2
    ltemp=[]
    for i in l1: 
        for x in l2:
            ltemp.append(x+i)
    return mer(l1,ltemp,n-1)     

print(mer(l1,l2,n))
