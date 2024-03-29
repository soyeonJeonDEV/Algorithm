#미로탐색
#https://www.acmicpc.net/problem/2178

from collections import deque

n,m = map(int,input().split())

graph = [list(map(int,input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def bfs(a,b):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  q = deque()
  q.append([a,b])
  visited[a][b] = 1

  while q:
    x,y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<m:
        if graph[nx][ny] == 1 and visited[nx][ny] == 0:
          visited[nx][ny] = visited[x][y] + 1
          q.append([nx,ny])
  return visited[n-1][m-1]

print(bfs(0,0))