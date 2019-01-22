# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 06:03:35 2019

@author: v-jaimo
"""

''' nPr Write a program to calculate nPr. nPr represents n permutation r and value of nPr is (n!) / (n-r)!. '''

def fact(n):
    if((n == 1) | (n == 0)):
        return 1
    else:
        return n * fact(n-1)

output = []

T = int(input())

if((T >= 1) & (T <= 100)):
    for i in range(T):
        n, r = input().split()
        n = int(n)
        r = int(r)
        if(n >= r):
            npr = fact(n)/fact(n-r)
            npr = int(npr)
            output.append(npr)

for i in output:
    print(i)
    
    