# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 07:04:54 2019

@author: v-jaimo
"""

rows = int(input())
cols = int(input())

welcome_line = cols - 7

string = "ABCDCDC"
substring = "CDC"

position = 0
count = 0
while(position != -1):
    position = string.find(substring, position)
    if(position != -1):
        count += 1
        position += 1

    
s = input()
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.islower())
print(s.isupper())