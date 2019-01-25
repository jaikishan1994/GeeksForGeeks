# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 00:02:17 2019

@author: v-jaimo
"""

'''
GCD of Array
'''

def gcd(a,b):
    '''
    Euclidian algorithm to find the GCD of 2 numbers
    '''
    if(a == b):
        return a
    if(a > b):
        return gcd(a-b,b)
    if(a < b):
        return gcd(a,b-a)

def array_GCD(a):
    '''
    This method propagates through the array by picking first two digits and replacing it with its GCD
    '''
    while(len(a) > 1):
        n1 = a[0]
        n2 = a[1]
        a[1] = gcd(n1,n2)
        a = a[1:]
    return a
   
output = []

T = int(input())
if((T >= 1) & (T <= 100)):
    for i in range(T):
        #input the size of the array
        n = int(input())
        if((n >= 1) & (n <= 10 ** 6)):
            #input array a
            a = [int(i) for i in input().split()]
            value = array_GCD(a)
            vv = value[0]
            output.append(vv)
    
    for i in output:
        print(i)
            
    
    