#점프왕 쩰리
#https://www.acmicpc.net/problem/16173
from collections import deque

def bfs(x,y):
  q = deque()
  q.append([x,y])
  visit = [[0]*n for _ in range(n)]

  while q:
    x,y = q.popleft()
    go = graph[x][y]

    if graph[x][y] == -1:
      return "HaruHaru"

    for i in range(4):
      nx = x+dx[i]*go
      ny = y+dy[i]*go
      if 0<=nx<n and 0<=ny<n:
        if visit[nx][ny] == 0:
          visit[nx][ny] = 1
          q.append([nx,ny])


  else:
    return "Hing"  

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))

