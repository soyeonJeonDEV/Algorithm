#미로탐색
#https://www.acmicpc.net/problem/2178

from collections import deque

n,m = map(int,input().split())

graph = [list(map(int,input())) for _ in range(n)]
visited = [[0 for _ in range(m) for _ in range(n)]

def bfs(x,y):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  queue = deque([x,y])
  visited[x][y] = 1

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
<<<<<<< HEAD
      if 0< nx <= n and 0 < ny <= m:
=======
      if 0< nx <= n and o < ny <= m:
>>>>>>> 5fba878666ee95be4e927f16de77e5cfe4e0f58e
        if graph[nx][ny] == 1 and visited[nx][ny] == 0:
          queue.append([nx,ny])
          visited[nx][ny] = visited[x][y] + 1
  return visited[n-1][m-1]
  
print(bfs(0,0))