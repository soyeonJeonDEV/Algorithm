#https://www.acmicpc.net/problem/1303
#전쟁-전투
from collections import deque

n,m = map(int,input().split())
graph = [list(map(str,input())) for _ in range(m)]
visited = [[False]*n for _ in range(m)]

def bfs(a,b,color):
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

            if 0<=nx<n and 0<=ny<m:
                if not visited[ny][nx] and graph[ny][nx] == color:
                    visited[ny][nx] = True
                    q.append((ny,nx))
                    cnt += 1
    return cnt
team1 = 0
team2 = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' and not visited[i][j]:
            visited[i][j] = True
            team1 += (bfs(i,j,'W'))**2

        elif graph[i][j] == 'B' and not visited[i][j]:
            visited[i][j] = True
            team2 += (bfs(i,j,'B'))**2
print(team1, team2)
