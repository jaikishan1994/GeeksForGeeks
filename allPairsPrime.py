# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 02:46:44 2019

@author: Kish
"""
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

def enumerate_pairs(a,n):
    '''
    Enumerating all possible pairs (p,q) where p*q <= n
    '''
    pairs = []
    for i in range(len(a)):
        for j in range(len(a)):
            if(a[i]*a[j] <= n):
                #print(a[i],a[j])
                #here I'm assuming each pair as a tuple and adding it to the pairs list
                t = (a[i],a[j])
                pairs.append(t)
    return pairs

#a = [2,3,5,7]
#n = 8
#p = enumerate_pairs(a,n)

T = int(input())

a = numpy.array([])

primeNumbers = []
allPrimePairs = []

if((T >= 1) & (T <= 50)):
    for i in range(T):
        n = int(input())
        if((n >= 4) & (n <= 400)):
            a = numpy.arange(0,n+1)
            primeNumbers.append(sieve(a,n))
    #print(primeNumbers)
            allPrimePairs.append(enumerate_pairs(primeNumbers[i],n))
    #print(primeNumbers)
    #print(allPrimePairs)
    for i in allPrimePairs:
        for j in i:
            for k in j:
                print(k,end=" ")
        print("")

#As the GFG IDE is inputing a sigle input n, so adding this piece of chunk to just satisfy thier IDE 
#else my code till here works fine
if(T > 50):
    n = T
    T = 1
    for i in range(T):
        if((n >= 4) & (n <= 400)):
            a = numpy.arange(0,n+1)
            primeNumbers.append(sieve(a,n))
    #print(primeNumbers)
            allPrimePairs.append(enumerate_pairs(primeNumbers[i],n))
    #print(primeNumbers)
    #print(allPrimePairs)
    for i in allPrimePairs:
        for j in i:
            for k in j:
                print(k,end=" ")
        print("")
