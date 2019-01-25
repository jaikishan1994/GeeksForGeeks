# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:55:41 2019

@author: v-jaimo
"""

''' Closest number
print the closest number to N which is also divisible by M
'''

def closest(n,m):
    q = int(n/m)
    if((n*m) > 0):
        v2 = m * (q + 1)
    else:
        v2 = m * (q - 1)
    
    v1 = m * q
    #whichever closest to difference of v1-n and v2-n
    if(abs(n - v1) < abs(n - v2)):
        return v1
    return v2
    

output = []

T = int(input())

if((T >= 1) & (T <= 100)):
    for i in range(T):
        N, M = input().split()
        N = int(N)
        M = int(M)
        if((N >= -1000) & (M <= 1000)):
            output.append(closest(N,M))
        
    for i in output:
        print(i)
