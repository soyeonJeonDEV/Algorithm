#유기농배추
#https://www.acmicpc.net/problem/1012
from collections import deque
def bfs(a,b):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  q = deque()
  q.append([a,b])
  graph[a][b] = 0

  while q:
    y,x = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<m and 0<=ny<n:
        if graph[ny][nx] == 1:
          graph[ny][nx] = 0
          q.append([ny,nx])


t = int(input())
for i in range(t):
  m,n,k = map(int,input().split())
  graph = [[0]*m for _ in range(n)]
  cnt = 0

  for j in range(k):
    x,y = map(int,input().split())
    graph[y][x] = 1

  for o in range(n):
    for p in range(m):
      if graph[o][p] == 1:
        bfs(o,p)
        cnt += 1

  print(cnt)