# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 00:57:02 2019

@author: v-jaimo
"""

'''
Given the first 2 terms A and B of an Arithmetic Series, tell the Nth term of the series. 
'''

#No.of test cases
testcases = int(input())

Nterm = []

if(testcases > 0 & testcases <= 100):
    for i in range(testcases):
        A, B = input().split()
        A = int(A)
        B = int(B)
        N = int(input())
        
        #Validate the constraints
        if((A >= -1000) & (A <= 1000) & (B >= -1000) & (B <= 1000) & (N >= 1) & (N <= 10000)):
            #difference of first two terms in AP 'd'
            d = B - A
            #Nth term in AP
            x = A + ((N-1) * d)
            Nterm.append(x)
        else:
            #report an error
            exit(-1)

for val in Nterm:    
    print(val)