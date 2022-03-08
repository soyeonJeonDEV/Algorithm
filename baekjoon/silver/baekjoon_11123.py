# 양 한마리... 양 두마리

from collections import deque

t = int(input())

def bfs(a,b):

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    q = deque()
    q.append((a,b))

    while q:
        y,x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<w and 0<=ny<h:
                if graph[ny][nx] == '#' and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    q.append((ny,nx))
for _ in range(t):
    h,w  = map(int,input().split())

    graph = [list(map(str,input())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == False and graph[i][j] == '#':
                visited[i][j] == True
                bfs(i,j)
                cnt += 1

    print(cnt)

    