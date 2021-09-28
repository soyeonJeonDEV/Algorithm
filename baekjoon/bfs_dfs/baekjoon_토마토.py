#토마토
#https://www.acmicpc.net/problem/7576
from collections import deque

def bfs(x,y):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  q = deque()
  q.append([x,y])

  while q:
    y,x = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<m and 0<=ny<n:
        if graph[ny][nx] == 0:
          q.append([ny,nx])
          graph[ny][nx] = graph[y][x] + 1
          
m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      bfs(i,j)
print(graph)
total = graph[0][0]
endFlag = False

for i in range(n):
  for j in range(m):
    if graph[i][j] != 0:
      total = max(graph[i][j],total)
    else:
      print(-1)
      endFlag = True
      break
  if endFlag:
    break
if not endFlag:
  print(total-1)
  





