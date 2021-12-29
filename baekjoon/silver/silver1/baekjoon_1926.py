#https://www.acmicpc.net/problem/1926
#그림

from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

answer = []
def bfs(a,b):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    q = deque()
    q.append([a,b])
    cnt = 1

    while q:
        y,x = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    cnt += 1
                    q.append([ny,nx])


    answer.append(cnt)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 0
            bfs(i,j)

if answer:
    print(len(answer))
    print(max(answer))
else:
    print(0)
    print(0)
    
