# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:39:05 2019

@author: v-jaimo
"""

''' LCM/GCD of two number A and B 
Logic: A*B = GCD(A,B) * LCM (A,B)
Eg:
    10*5 = GCD(10,5) * LCM(10,5)
        = 5 * 10 = 50

'''

def gcd(a,b):
    if(a==b):
        return a
    if(a>b):
        return gcd(a-b,b)
    if(a<b):
        return gcd(a,b-a)

def lcm(a,b):
    return int((a*b)/gcd(a,b))

output_gcd = []
output_lcm = []

T = int(input())

if((T >= 1) & (T <= 30)):
    for i in range(T):
        A, B = input().split()
        A = int(A)
        B = int(B)
        _gcd = gcd(A,B)
        output_gcd.append(_gcd)
        output_lcm.append(int((A*B)/_gcd))

    for i in range(T):
        print(output_lcm[i],output_gcd[i])

    