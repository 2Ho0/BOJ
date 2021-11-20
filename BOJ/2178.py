from collections import deque
n,m = map(int, input().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    graph.append(list(map(int,input())))

def maze(x,y):
    que = deque()
    que.append((x,y))

    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                que.append((nx,ny))
                graph[nx][ny]= graph[x][y]+1
    return graph[n-1][m-1]

print(maze(0,0))