#https://www.acmicpc.net/problem/1743
#음식물 피하기

from collections import deque

n,m,k = map(int,input().split())
graph = [[0]*m for _ in range(n)]

for i in range(k):
    y,x = map(int,input().split())
    graph[y-1][x-1] = 1

visited = [[False]*m for _ in range(n)]
def bfs(a,b):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    q = deque()
    q.append((a,b))
    cnt = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    cnt += 1
                    q.append((ny,nx))
    return cnt
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            answer = max(answer, bfs(i,j))
print(answer)