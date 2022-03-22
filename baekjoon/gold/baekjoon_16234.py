import sys
from collections import deque

# 한 나라를 지정하고 4방향으로 인구수를 조사하여 국경을 열거나 닫는다
# 국경이 열렸다면 인구 이동을 시작한다
# 열린 국가만 인구이동을 통해 인구를 나눈다. 소수점은 버린다.
# 인구가 모든 나라가 같은 때까지 반복

input = sys.stdin.readline

n,l,r = map(int,input().split())

country = [[] for _ in range(n)]
for i in range(n):
    r,c = map(int,input().split())
    country[i].append(r) 
    country[i].append(c)

visited = [[False]*n for _ in range(n)]


def bfs(a,b,graph, visit):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    q = deque()
    q.append([a,b])


    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if l <= abs(country[x][y] - country[nx][ny]) <= r and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append([nx,ny])
day = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]: 
            bfs(i,j)
            day += 1

temp = 0