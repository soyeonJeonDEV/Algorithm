#토마토
#https://www.acmicpc.net/problem/7576
from collections import deque

def bfs():
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  q = deque()

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        q.append([i,j])

  while q:
    y,x = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<m and 0<=ny<n:
        if graph[ny][nx] == 0:
          graph[ny][nx] = graph[y][x] + 1
          q.append([ny,nx])

  for i in graph:
    if 0 in i:
        return -1
  day = max(map(max,graph))
  return day -1

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

print(bfs())