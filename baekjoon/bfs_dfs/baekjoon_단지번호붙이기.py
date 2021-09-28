#단지번호붙이기
#https://www.acmicpc.net/problem/2667
from collections import deque

def bfs(x,y):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  q = deque()
  q.append([x,y])
  cnt = 1

  while q:
    x,y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<n:
        if graph[nx][ny] == 1:
          graph[nx][ny] = 0
          q.append([nx,ny])
          cnt += 1

  b_cnt.append(cnt)

n = int(input())
graph = [list(map(int,input()))for _ in range(n)]
num = 0
b_cnt = []

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      graph[i][j] = 0
      bfs(i,j)
      num += 1 

print(num)
b_cnt = sorted(b_cnt)
for i in b_cnt:
  print(i)
