# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 01:55:27 2019

@author: Kish
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:39:05 2019

@author: v-jaimo
"""

''' LCM/GCD of two number A and B 
Logic: A*B = GCD(A,B) * LCM (A,B)
Eg:
    10*5 = GCD(10,5) * LCM(10,5)
        = 5 * 10 = 50

'''

def gcd(a,b):
    if(a==b):
        return a
    if(a>b):
        return gcd(a-b,b)
    if(a<b):
        return gcd(a,b-a)

def lcm(a,b):
    return int((a*b)/gcd(a,b))

def addFraction(num1, den1, num2, den2):
    output_num = []
    output_den = []
    
    num1 = int(num1)
    den1 = int(den1)
    num2 = int(num2)
    den2 = int(den2)
    _gcd = gcd(den1,den2)
    _lcm = int((den1*den2)/_gcd)
    output_num.append((num1 * (int(_lcm/den1))) + (num2 * (int(_lcm/den2))))
    output_den.append(_lcm)
        
    gcd_numden = gcd(output_num[0],output_den[0])
    #print(int(output_num[0]/gcd_numden),'/',int(output_den[0]/gcd_numden))        
    print("{0}/{1}".format(int(output_num[0]/gcd_numden),int(output_den[0]/gcd_numden)))