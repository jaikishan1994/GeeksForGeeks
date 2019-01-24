# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 06:25:34 2019

@author: v-jaimo
"""

'''
GCD of two numbers
Euclidian algorithm to find the GCD of two numbers
'''
def gcd(a,b):
    if(a>b):
        return gcd(a-b,b)
    if(a<b):
        return gcd(a,b-a)
    if(a==b):
        return a;

output = []

T = int(input())

if((T >= 1) & (T <= 100)):
    for i in range(T):
        A, B = input().split()
        A = int(A)
        B = int(B)
        if((A >= 1) & (B <= 1000)):
            output.append(gcd(A,B))

for val in output:
    print(val)
        
        
        
        
