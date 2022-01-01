#https://www.acmicpc.net/problem/1012
#유기농 배추
from collections import deque
t = int(input())

def bfs(a,b):
    dy = [0,1,0,-1]
    dx = [-1,0,1,0]
    q = deque()
    q.append([a,b])

    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    q.append([ny,nx])

for i in range(t):
    n,m,k = map(int,input().split())
    graph = [[0]*n for _ in range(m)]
    cnt = 0
    for _ in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1
    for j in range(m):
        for k in range(n):
            if graph[j][k] == 1:
                graph[j][k] = 0
                bfs(j,k)
                cnt += 1


    print(cnt)
    
