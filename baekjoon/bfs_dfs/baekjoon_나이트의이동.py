#나이트의 이동
#https://www.acmicpc.net/problem/7562
from collections import deque

T = int(input())

for i in range(T):
  l = int(input())
  x, y = map(int,input().split())
  rx, ry = map(int,input().split())
  visited = [[0]*l for _ in range(l)]

  dx = [2,1,-1,-2,-2,-1,1,2]
  dy = [1,2,2,1,-1,-2,-2,-1]
  queue = deque()
  queue.append([x,y])

  while queue:
    x,y = queue.popleft()

    if x == rx and y == ry:
      break

    for i in range(8):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0<=nx<l and 0<=ny<l:
        if visited[nx][ny] == 0:
          visited[nx][ny] = visited[x][y] + 1
          queue.append([nx,ny])
  
  print(visited[rx][ry])