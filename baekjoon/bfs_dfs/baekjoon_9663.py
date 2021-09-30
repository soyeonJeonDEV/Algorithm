#N-Queen
#https://www.acmicpc.net/problem/9663
from collections import deque

def bfs(i,j):
    q = deque()
    q.append([i,j])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 0:
                    graph

n = int(input())
graph = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        graph[i][j] = 1
        bfs(i,j)
