from collections import deque


c,r = map(int,input().split())

graph = [list(map(str, input())) for _ in range(c)]
visited = [[0]*r for _ in range(c)]

wolf = 0
sheep = 0

def bfs(a,b):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    q = deque()
    q.append((a,b))
    global w, s

    while q:
        x,y = q.popleft()

        if graph[x][y] == 'v':
            w += 1
        elif graph[x][y] == 'o':
            s += 1
        
        graph[x][y] = '#'

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<c and  0<=ny<r:
                if not visited[nx][ny] and graph[nx][ny] != '#':
                    visited[nx][ny] = 1
                    q.append((nx,ny))

                


for i in range(c):
    for j in range(r):
        if not visited[i][j] and graph[i][j] != '#':
            visited[i][j] = 1
            w = 0
            s = 0
            bfs(i,j)
            if w >= s:
                s = 0
            else:
                w = 0

            wolf += w
            sheep += s

print(sheep, wolf)
           

