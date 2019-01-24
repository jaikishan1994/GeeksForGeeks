# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:51:27 2019

@author: Kish
"""

'''
Closest Number
'''

def closest(n,m):
    q = int(n/m)
    n1 = q * m
    if((n*m) < 0):
        #Because the quotient will be negative
        n2 = m * (q-1)
    else:
        n2 = (q+1) * m
    if(n%m == 0):
        return n
    if(abs(n - n1) < abs(n - n2)):
        return n1
    return n1
    
    
output = []

T = int(input())

if((T >= 1)&(T <= 100)):
    for i in range(T):
        n,m = input().split()
        n = int(n)
        m = int(m)
        output.append(closest(n,m))
    
    for i in output:
        print(i)
