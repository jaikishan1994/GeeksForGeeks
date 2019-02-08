# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 03:01:34 2019

@author: v-jaimo
"""
students = []
for i in range(int(input())):
    name = input()
    score = float(input())
    students.append(list({name,score}))

for i in students:
    min1 = students[i][1]
    min2 = students[i+1][1]
    
    if(students[i+2] < min):
        min = students[i][1]
        student = students[i][0]
            
    
        
    
j = [['Rachel',-50],['Mawer',-50],['Sheen',-50],['Shaheen',51]]
    
j = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
j.sort(key = lambda x:x[1])

#remove the least marks student record from the list
min_stud = min(j,key = lambda x:x[1])
min_mar = min_stud[1]
i = 0
while (i < len(j)):
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
while (i < len(j)):
    min_stud = min(j,key = lambda x:x[1])
    if(min_stud[1] == min_mar):
        output.add(min_stud[0])
    i += 1

for i in output:
    print(i)

    
    


