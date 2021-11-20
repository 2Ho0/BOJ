import sys
import copy
n = int(input())
m = []
result = []
for i in range(n):
    m.append(list(map(int, input().split())))
for i in range(3*2**(n-1)):
    result.append(0)


for k in range(3):
    mc = copy.deepcopy(m)
    j = 1
    h = m[0][k]
    result[k]+=h
    for a in range(1,n):
        if j == n:
            break
        if mc[j].index(min(mc[j]))==mc[j-1].index(min(mc[j-1])):
            mc[j][mc[j].index(min(mc[j]))]=1001
            continue
        result[k]+=min(mc[j])
        j+=1

print(min(result))