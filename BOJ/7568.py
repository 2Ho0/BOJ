"""import sys

n = int(input())

m = []
max_m = []

rank = 1
count=0
reverse = 0
for i in range(n):
    m.append(list(map(int, sys.stdin.readline().split())))
    max_m.append(0)

for j in range(n):
    max1 = m[0][0]
    max2 = m[0][1]
    ind1 = 0
    ind2 = 0
    for a in range(len(m)-1):
        if max1<m[a+1][0]:
            max1 = m[a+1][0]
            ind1 = a+1
    for b in range(len(m)-1):
        if max2<m[b+1][1]:
            max2 = m[b+1][1]
            ind2 = b+1
    if max1==0 and max2==0:
        break

    if ind1 == ind2:
        if reverse==1:
            max_m[ind2]= rank
        if reverse==0:
            max_m[ind2] = rank+count
        rank+=1
        m[ind2][0] = 0
        m[ind2][1] = 0
        reverse = 0

    elif ind1!=ind2:
        if reverse == 1:
            rank+=1
            max_m[ind1] = rank
            max_m[ind2] = rank
        if reverse == 0:
            max_m[ind1] = rank
            max_m[ind2] = rank

        m[ind1][0] = 0
        m[ind1][1] = 0
        m[ind2][0] = 0
        m[ind2][1] = 0

        count+=2
        reverse = 1

for i in range(n):
    if i == n-1:
        print(max_m[i])
    else:
        print(max_m[i], end=' ')"""

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
for user in data:
    count: int = list(map(lambda x: x[0] > user[0] and x[1] > user[1], data)).count(True)
    print(count + 1, end=" ")
print()