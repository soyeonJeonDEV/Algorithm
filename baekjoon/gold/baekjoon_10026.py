#https://www.acmicpc.net/problem/10026
#적록색약

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [list(map(str,input())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
def bfs(a,b,color):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    q = deque()
    q.append([a,b])

    while q:
        y,x = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[ny][nx] == color and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([ny,nx])
#적록색약이 아닌사람
cnt1 = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R' and visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i,j,'R')
            cnt1 += 1
        elif graph[i][j] == 'B' and visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i,j,'B')
            cnt1 += 1
        elif graph[i][j] == 'G' and visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i,j,'G')
            cnt1 += 1

#적록색약인 사람
cnt2 = 0
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'           
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R' and visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i,j,'R')
            cnt2 += 1
        elif graph[i][j] == 'B' and visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i,j,'B')
            cnt2 += 1
print(cnt1, cnt2)