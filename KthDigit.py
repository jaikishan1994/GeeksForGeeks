# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 23:52:04 2019

@author: v-jaimo
"""

'''
Print Kth Digit
Given two numbers A and B, find Kth digit from right of AB.
'''

output = []

T = int(input())

if((T >= 1) & (T <= 100)):
    for i in range(T):
        a, b, k = input().split()
        a = int(a)
        b = int(b)
        k = int(k)
        if((a >= 1) & (b <= 15)):
            value = int(a ** b)
            digits = len(str(value))
            if((k >= 1) & (k <= digits)):
                for i in range(k):
                    x = value % 10
                    value = int(value/10)
                output.append(x)
                    
    for i in output:
        print(i)
    
