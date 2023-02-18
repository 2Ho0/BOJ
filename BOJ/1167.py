from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
a = [[] for _ in range(n+1)]

for i in range(n):
    data = list(map(int, input().split()))
    index = 0
    s = data[index]
    index+=1
    while True:
        e = data[index]
        if e == -1:
            break
        v = data[index+1]
        a[s].append((e,v))
        index+=2

distance = [0]*(n+1)
visited = [False]*(n+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        tree = queue.popleft()
        for i in a[tree]:
            if not visited[i[0]]:
                visited[i[0]]=True
                queue.append(i[0])
                distance[i[0]] = distance[tree] + i[1]
BFS(1)

maxdis = distance.index(max(distance))
distance = [0]*(n+1)
visited = [False]*(n+1)
BFS(maxdis)

print(max(distance))