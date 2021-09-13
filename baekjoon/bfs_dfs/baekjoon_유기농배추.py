#유기농배추
#https://www.acmicpc.net/problem/1012

def dfs(y,x):

  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<= ny < n and 0<= nx < m:
      if graph[ny][nx] == 1:
        graph[ny][nx] = -1
        dfs(ny,nx)

T = int(input())
counts = []

for _ in range(T):
  m,n,k = map(int, input().split())
  graph = [[0]*m for _ in range(n)]
  count = 0

  for _ in range(k):
    x,y = map(int,input().split())
    graph[y][x] = 1

  for y in range(n):
    for x in range(m):
      if graph[y][x] == 1:
        dfs(y,x)
        count += 1

  counts.append(count)

for cnt in counts:
  print(cnt)


