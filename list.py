# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 02:12:11 2019

@author: v-jaimo
"""

N = int(input())
li = []
output = []
for line in range(N):
    cmd, *values = input().split()
    if(cmd == 'insert'):
        i = int(values[0])
        v = int(values[1])
        li.insert(i,v)
    if(cmd == 'print'):
        output.append(list(li))
    if(cmd == 'remove'):
        v = int(values[0])
        if(v in li):
            li.remove(v)
    if(cmd == 'pop'):
        li.pop()
    if(cmd == 'sort'):
        li.sort()
    if(cmd == 'append'):
        v = int(values[0])
        li.append(v)
    if(cmd == 'reverse'):
        li.reverse()

for i in output:
    print(i)