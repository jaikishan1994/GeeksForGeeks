# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 04:14:48 2019

@author: v-jaimo
"""

'''
Sum of Digit is Pallindrome or not
'''

output = []

# read testcases  T
T = int(input())

if((T >= 1) & (T <= 200)):
    
    #iterate through the each test case
    for i in range(T):
        #read the number
        N = int(input())
        #validate the constraints
        if((N >= 1) & (N <= 1000)):
            sum = 0
            while(N != 0):
                sum = sum + N % 10
                N = int(N/10)
            
            if(str(sum) == str(sum)[::-1]):
                output.append('YES')
            else:
                output.append('NO')

for val in output:
    print(val)