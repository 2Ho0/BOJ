import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
stack = [0]
ans = [-1]*n

for i in range(1,n):
    while stack and a[stack[-1]] < a[i]:
        ans[stack.pop()] = a[i]
    stack.append(i)
    
print(*ans)