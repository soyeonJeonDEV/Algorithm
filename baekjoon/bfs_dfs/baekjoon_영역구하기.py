#영역 구하기
#https://www.acmicpc.net/problem/2583
from collections import deque

def bfs(a,b):
  queue = deque()
  queue.append([a,b])
  global cnt
  while queue:
    y,x = queue.popleft()

    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0<=nx<m and 0<= ny <n:
        if graph[ny][nx] == 0:
          cnt += 1
          graph[ny][nx] = 1
          queue.append([ny,nx])

m,n,k = map(int,input().split())
graph = [[0]*m for _ in range(n)]

for i in range(k):
  x,y,rx,ry = map(int,input().split())
  for a in range(x,rx):
    for b in range(y,ry):
      graph[a][b] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0
counts =[]

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      cnt = 1
      graph[i][j] = 1
      count += 1
      bfs(i,j)
      counts.append(cnt)
counts.sort()

print(count)
for i in range(len(counts)):
  print(counts[i], end = " ")
      