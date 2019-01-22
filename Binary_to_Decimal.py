# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 04:33:33 2019

@author: v-jaimo
"""

'''Binary number to decimal number'''


output = []

# read testcases  T
T = int(input())

if((T > 1) & (T < 100)):
    
    #iterate through the each test case
    for i in range(T):
        #read the number in binary using the parameter base2
        N = int(input(),2)
        output.append(N)

for val in output:
    print(val)
