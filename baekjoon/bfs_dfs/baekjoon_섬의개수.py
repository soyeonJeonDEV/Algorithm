#섬의 영역
#https://www.acmicpc.net/problem/4963
'''
상하좌우
dx=[1,0,-1,0]
dy=[0,1,0,-1]
대각선
dx=[-1,-1,1,1]
dy=[-1,1,-1,1]
대각선+상하좌우
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]
'''
from collections import deque
import sys
sys.setrecursionlimit(10000)

def bfs(a,b):
  queue = deque()
  queue.append([a,b])

  while queue:
    y, x = queue.popleft()
    
    for i in range(8):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0<=nx<w and 0<=ny<h and graph[ny][nx] == 1:
        graph[ny][nx] = 0
        queue.append([ny,nx])


dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]
counts = []

while True:
  w,h = map(int,input().split())
  graph = [list(map(int,input().split())) for _ in range(h)]

  if w == 0 or h == 0:
    break

  count = 0

  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        graph[i][j] = 0
        bfs(i,j)
        count += 1

  counts.append(count)

for i in range(len(counts)):
  print(counts[i])