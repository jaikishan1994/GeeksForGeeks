# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 02:14:55 2019

@author: v-jaimo
"""

#Armstrong Numbers

# read testcases  T
T = int(input())

if((T >= 1) * (T <= 31)):
    
    #iterate through the each test case
    for i in range(T):
        #read the number
        N = int(input())
        #validate the constraints
        if((N >= 100) * (N <= 1000)):
            
            
            print('valid')

