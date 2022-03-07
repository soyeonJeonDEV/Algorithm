# 현수막
# https://www.acmicpc.net/problem/14716

from collections import deque

n,m = map(int,input().split())

graph =[list(map(int,input().split())) for _ in range(n) ]


def bfs(a,b):
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]

    q = deque()
    q.append((a,b))

    while q:
        y,x = q.popleft()
        for i in range(8):
            nx = x +dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    q.append((ny,nx))

cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 0
            bfs(i,j)
            cnt += 1

print(cnt)