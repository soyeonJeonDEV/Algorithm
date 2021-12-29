#https://www.acmicpc.net/problem/2667
#단지번호붙이기
import sys
from collections import deque

n = int(input())
graph = [list(map(int,input()))for _ in range(n)]
answer = []

def bfs(a,b):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    cnt = 1 

    q = deque()
    q.append([a,b])

    while q:
        y,x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    q.append([ny,nx])
                    cnt += 1
    answer.append(cnt)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = 0
            bfs(i,j)

print(len(answer))
answer.sort()
for i in answer:
    print(i)

