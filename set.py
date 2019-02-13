# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

input = []
for line in sys.stdin:
    input.append(line)

m = int(input[0])
m_set = set(map(int,(input[1].split())))
n = int(input[2])
n_set = set(map(int,(input[3].split())))

#print('m',m)
#print('m set',m_set)
#print('n : ',n)
#print('n set:',n_set)

output = set((m_set - n_set).union(n_set - m_set))
#print(output)
output = sorted(output)
#print(output)
for i in output:
    print(i)
    


# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

input = []
n = sys.stdin.readline()
for v in range(int(n)):
    for line in sys.stdin:
        input.append(line.strip())

input = set(input)
#print(input)
print(len(input))


#items_set = set(input.split())

#print('m',m)
#print('m set',m_set)
#print('n : ',n)
#print('n set:',n_set)

#output = set((m_set - n_set).union(n_set - m_set))
#print(output)
#output = sorted(output)
#print(output)

n = int(input())
s = set(map(int, raw_input().split()))
n_cmd = int(input())
for i in range(n_cmd):
    cmd = raw_input().split()
    if(cmd[0] == "pop"):
        s.pop()
    if(cmd[0] == "discard"):
        s.discard(int(cmd[1]))
    if(cmd[0] == "remove"):
        s.remove(int(cmd[1]))

print(sum(s))
