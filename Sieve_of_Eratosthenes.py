# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 10:42:33 2019

@author: Kish
"""

'''
Sieve of Eratosthenes
'''
import numpy

def sieve(a,n):
    result = []
    setPrime = numpy.array(a)
    for i in range(2,n+1):
        setPrime[i] = 1
    
    for i in range(2,n+1):
        if(setPrime[i] == 1):
            j = 2
            while((i*j) <= n):
                if(setPrime[j*i] == 1):
                    setPrime[j*i] = 0
                j += 1
            
    for i in range(2,n+1):
        if(setPrime[i] == 1):
            result.append(i)
    
    return result

T = int(input())

a = numpy.array([])

output = []
if((T >= 1) & (T <= 100)):
    for i in range(T):
        n = int(input())
        if((n >= 1) & (n <= 10**4)):
            #Create an array of n integers
            a = numpy.arange(0,n+1)
            output.append(sieve(a,n))
    
    for i in range(len(output)):
        for j in output[i]:
            print(j,end = " ")
        print("")
    
            

        
    