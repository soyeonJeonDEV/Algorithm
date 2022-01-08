#https://www.acmicpc.net/problem/2178
#미로탐색

from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def bfs(a,b):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    q = deque()
    q.append((a,b))
    visited[a][b] = True

    while q:
        y , x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    graph[ny][nx] = graph[y][x] + 1
                    q.append((ny,nx))
    
bfs(0,0)
print(graph[-1][-1])