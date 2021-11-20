from math import sqrt
n, k = map(int, input().split())
m = []
count = 0
for i in range(n):
    m.append(i+1)

for i in range(2,n+1):
    if i not in m:
            continue
    else:
        m.remove(i)
        count+=1
    if count == k:
            print(i)
            exit(0)
    for j in range(i*i, n+1, i):
        if j not in m:
            continue
        else:
            m.remove(j)
            count +=1
            if count == k:
                print(j)
                exit(0) 
