import math
n = int(input())
m = []
count = 0
m.append(math.factorial(n))

for i in reversed(str(m[0])):
    if i=='0':
        count+=1
    else:
        print(count)
        exit(0)

