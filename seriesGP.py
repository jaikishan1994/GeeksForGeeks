# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 22:50:23 2019

@author: v-jaimo
"""

'''
Series GP
Given the first 2 terms A and B of a Geometric Series, tell the Nth term of the series.
'''
import math

def nthTermGP(a,b,n):
    r = b/a
    if(n == 1):
        # return the first term
        return a;
    else:
        return (a * r**(n-1))
    
    
output = []

T = int(input())
if((T >= 1) & (T <= 30)):
    for i in range(T):
        a, b = input().split()
        a = int(a)
        b = int(b)
        if((a >= -100) & (a <= 100) & (b >= -100) & (b <= 100)):
            n = int(input())
            if((n >= 1) & (n <= 5)):
                output.append(math.floor(nthTermGP(a,b,n)))
        
    for i in output:
        print(i)
                    