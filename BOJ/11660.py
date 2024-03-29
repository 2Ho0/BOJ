import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[0]*(n+1)]
s = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    al = [0] + [int(x) for x in input().split()]# [0] + list(map(int, input().split())) 이렇게 써도 상관X
    a.append(al)

for i in range(1,n+1):
    for j in range(1,n+1):
        s[i][j] = s[i][j-1]+s[i-1][j]-s[i-1][j-1]+a[i][j]
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = s[x2][y2]-s[x1-1][y2]-s[x2][y1-1]+s[x1-1][y1-1]
    print(answer)

