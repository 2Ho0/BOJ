n = int(input())
a = list(map(int, input().split()))

s = [0]*n
for i in range(1,n):
    point = i
    value = a[i]
    for j in range(i-1,-1,-1):
        if a[j]<a[i]:
            point = j+1
            break
        if j == 0:
            point = 0
    for j in range(i, point, -1):
        a[j] = a[j-1]
    a[point] = value

s[0] = a[0]

for i in range(1,n):
    s[i] = s[i-1]+a[i]
print(sum(s))
