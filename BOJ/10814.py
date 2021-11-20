n = int(input())
m = []
for i in range(n):
    m.append(list(map(str, input().split())))
    m[i][0]=int(m[i][0])
result = sorted(m, key = lambda x: x[0])

for i in range(n):
    print(result[i][0], result[i][1])
   