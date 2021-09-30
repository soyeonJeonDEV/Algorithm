#백조의 호수
#https://www.acmicpc.net/problem/3197
from collections import deque

r,c = map(int,input().split())
graph = [list(map(str,input())) for _ in range(r)]
water = deque()
swan = deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'L':
            swan.append([i,j])
            water.append([i,j])
        elif graph[i][j] == '.':
            water.append([i,j])

def bfs(water,swan,r,c,graph):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    endX, endY = swan.pop()
    time = 1

    while swan:
        temp = deque()
        while water:
            y,x = water.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<c and 0<=ny<r:
                    if graph[ny][nx] == 'X':
                        graph[ny][nx] = '.'
                        temp.append([ny,nx])
        
        water = temp

        temp = deque()
        
        while swan:
            y,x = swan.popleft()

            if y == endX and x == endY:
                return time

            if graph[y][x] == 'L':
                graph[y][x] = time

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<= nx<c and 0<=ny<r:
                    if graph[ny][nx] == '.' or graph[ny][nx] == 'L':
                        graph[ny][nx] = time
                        swan.append([ny,nx])
                        temp.append([ny,nx])
        swan = temp
        time += 1
    return time

print(bfs(water,swan,r,c,graph))