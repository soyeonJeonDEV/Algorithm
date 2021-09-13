#단지번호붙이기
#https://www.acmicpc.net/problem/2667
from collections import deque

def bfs(x,y,cnt):
  queue = deque()
  queue.append(x,y)
  visited[x][y] =1 

  while queue:
    x,y = queue.popleft()

    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0<= nx < n and 0 <= ny <n:
        if graph[nx][ny] == 1 and visited == 0:
          queue.append([nx,ny])
          visited[nx][ny] = 1
          cnt_dict[cnt] += 1
          
n = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = [list(map(int,input())) for _ in range(n)]

visited[[0]*n for _in range(n)]

cnt = 0
cnt_dict={}

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and visited == 0:
      cnt += 1
      cnt_dict[cnt] = 1
      bfs(i,j,cnt)
print(cnt)