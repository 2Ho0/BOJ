import sys
from collections import deque

n = int(input())
que = deque()
for i in range(n):
    command = list(map(str,sys.stdin.readline().split()))
    if command[0] == "push":
        que.append(command[1])
    elif command[0] == "pop":
        if not que:
            print(-1)
        else:
            print(que.pop())
    elif command[0] == "size":
        print(len(que))
    elif command[0] == "empty":
        if not que:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if not que:
            print(-1)
        else:
            print(que[-1])
   