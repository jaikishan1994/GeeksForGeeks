# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 02:14:55 2019

@author: v-jaimo
"""

#Armstrong Numbers

output = []

# read testcases  T
T = int(input())

if((T >= 1) & (T <= 31)):
    
    #iterate through the each test case
    for i in range(T):
        #read the number
        N = int(input())
        #validate the constraints
        if((N >= 100) & (N < 1000)):
            temp = str(N) 
            value = int(temp[0:1]) ** 3 + int(temp[1:2]) ** 3 + int(temp[2:3]) ** 3
            
            if(int(value) == N):
                output.append('Yes')
            else:
                output.append('No')

for val in output:
    print(val)