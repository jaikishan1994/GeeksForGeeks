n = 17
x = len(bin(n)[2:])
for i in range(1,n+1):
    print(str(i).rjust(x)+oct(i)[2:].rjust(x)+hex(i)[2:].upper().rjust(x)+bin(i)[2:].rjust(x))
    
n = int(input())
student_marks = {}
for line in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

print("{0:.1f}".format(sum(student_marks[query_name])/n))

li = []
li.insert(0,5)
li.insert(1,10)
li.insert(0,6)
