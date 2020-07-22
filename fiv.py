#! /usr/bin/python3m
import sys

def fiv(n:int)->int:
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return fiv(n-1)+fiv(n-2) #이게 바로 재귀함수

n=int(sys.argv[1])
print(fiv(n))
