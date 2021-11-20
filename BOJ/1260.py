from collections import deque
import sys


n,m,start = map(int, input().split())

com = []
graph = [[0]]
visited = [False] * (n+1)
result_b = []
result_d = []
for i in range(m):
    co = list(map(int,sys.stdin.readline().split()))
    co.sort()
    com.append(co)

for k in range(n):
    graph.append([])
    for l in range(m):
        if k+1 in com[l]:
            if k+1==com[l][0]:
                graph[k+1].append(com[l][1])
            else:
                graph[k + 1].append(com[l][0])

for i in graph:
    i.sort()

def bfs(Graph, s, Visited):
    queue = deque([s])
    Visited[s] = True
    while queue:
        v = queue.popleft()
        result_b.append(v)
        for i in Graph[v]:
            if Visited[i] is False:
                queue.append(i)
                Visited[i] = True

def dfs(Graph, v, Visited):
    Visited[v] = True
    result_d.append(v)

    for i in Graph[v]:
        if Visited[i] is False:
            dfs(Graph, i, Visited)

visited_b = list(visited)
visited_d = list(visited)
dfs(graph,start, visited_d)
for i in result_d:
    print(i, end=" ")
print()
bfs(graph, start, visited_b)
for i in result_b:
    print(i, end=" ")

