n = int(input())
a = []

for i in range(n):
    a.append((int(input()), i))
    
s = sorted(a)
max = 0

for i in range(n):
    if max < s[i][1]-i:
        max = s[i][1]-i
print(max+1)