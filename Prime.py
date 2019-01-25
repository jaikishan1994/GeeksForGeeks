# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:28:57 2019

@author: v-jaimo
"""

def isPrime(n):
    for i in range(2,int(n/2)+1):
        if(n%i == 0):
            return 'No'
    return 'Yes'

output = []

T = int(input())

if((T >= 1) & (T <= 30)):
    for i in range(T):
        n = int(input())
        output.append(isPrime(n))

for val in output:
    print(val)