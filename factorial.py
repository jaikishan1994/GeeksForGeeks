# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 08:47:01 2019

@author: Kish
"""

# Factorial recursion

def fact(n):
    if((n==0) | (n==1)):
        return 1
    else:
        return n* fact(n-1)


output = []

T = int(input())

if((T >= 1) & (T <= 19)):
    for i in range(T):
        n = int(input())
        if((n >= 0) & (n <= 18)):
            output.append(fact(n))

for val in output:
    print(val)
