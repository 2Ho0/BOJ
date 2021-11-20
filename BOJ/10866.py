import sys
from collections import deque

n = int(input())
dq = deque([])
for i in range(n):
    command = list(map(str,sys.stdin.readline().split()))
    if command[0] == "push_front":
        dq.appendleft(command[1])
    elif command[0] == "push_back":
        dq.append(command[1])
    elif command[0] == "pop_front":
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    elif command[0] == "pop_back":
        if not dq:
            print(-1)
        else:
            print(dq.pop())
    elif command[0] == "size":
        print(len(dq))
    elif command[0] == "empty":
        if not dq:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif command[0] == "back":
        if not dq:
            print(-1)
        else:
            print(dq[-1])
        


