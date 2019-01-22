# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 06:13:58 2019

@author: v-jaimo
"""

'''
Reverse digits
'''

T = int(input())
output = []

if((T >=1 ) & (T <= 10**4)):
    for i in range(T):
        n = int(input())
        if((n >= 1) & (n <= 10**15)):
            n = str(n)
            n = n[::-1]
            n = int(n)
            output.append(n)

for i in output:
    print(i)
            
            
        