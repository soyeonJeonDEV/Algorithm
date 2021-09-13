#안전영역
#https://www.acmicpc.net/problem/2468

from collections import deque

def bfs(a,b):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  queue = deque()
  queue.append([a,b])
  sink[a][b] = 0

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0<=nx<n and 0<=ny<n and sink[nx][ny] == 1:
        queue.append([nx,ny])
        sink[nx][ny] = 0

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
max_value = 0
ans = 0

for i in range(n):
  for j in range(n):
    max_value = max(max_value, graph[i][j])

if max_value == 1:
  ans = 1
else:
  for day in range(max_value+1):
    sink = [[0]*n for _ in range(n)]
    for i in range(n):
      for j in range(n):
        sink[i][j] = 1 if graph[i][j] >= day else 0

    cnt = 0
    for i in range(n):
      for j in range(n):
        if sink[i][j] == 1:
          bfs(i,j)
          cnt += 1
    ans = max(ans,cnt)

print(ans)