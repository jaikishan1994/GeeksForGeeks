# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 00:15:13 2019

@author: v-jaimo
"""

n = int(input())
j = [[input(),float(input())] for i in range(n)]
j.sort(key = lambda x:x[1])

#remove the least marks student record from the list
min_stud = min(j,key = lambda x:x[1])
min_mar = min_stud[1]
i = 0
n = len(j)
while (i < n):
    min_stud = min(j,key = lambda x:x[1])
    if(min_stud[1] == min_mar):
        j.remove(min_stud)
    i += 1

# Now the list 'j' has removed the least marks student record
output = {}
output = set(output)

min_stud = min(j,key = lambda x:x[1])
min_mar = min_stud[1]
i = 0
l = len(j)
while (i < l):
    min_stud = min(j,key = lambda x:x[1])
    if(min_stud[1] == min_mar):
        j.remove(min_stud)
        output.add(min_stud[0])
    i += 1

output = list(output)
output.sort()
for i in output:
    print(i)


Rachel
-50
Mawer
-50
Sheen
-50
Shaheen
51