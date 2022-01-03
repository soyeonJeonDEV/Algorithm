#https://www.acmicpc.net/problem/2468
#안전 영역

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
t = 1

def bfs(a,b,t):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    q = deque()
    q.append([a,b])

    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[ny][nx] > t and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([ny,nx])

maxv = 1
while 1:
    cnt = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    if t > max(max(graph)):
        break
    for i in range(n):
        for j in range(n):
            if graph[i][j] > t and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i,j, t)
                cnt += 1
    maxv = max(cnt, maxv)
    t += 1
print(maxv)
