import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
a = list(map(int, input().split()))
mydeque = deque()

for i in range(n):
    while mydeque and mydeque[-1][1] > a[i]:
        mydeque.pop()
    mydeque.append((i,a[i]))
    if mydeque[0][0] <=i-l:
        mydeque.popleft()
    print(mydeque[0][1], end=' ')
