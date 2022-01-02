#https://www.acmicpc.net/problem/4963
#섬의 개수
import sys
from collections import deque

input = sys.stdin.readline

while 1:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0

    def bfs(a,b):
        dx = [-1,-1,0,1,1,1,0,-1]
        dy = [0,1,1,1,0,-1,-1,-1]
        q = deque()
        q.append([a,b])

        while q:
            y,x = q.popleft()

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<= nx<w and 0<= ny <h:
                    if graph[ny][nx] == 1:
                        graph[ny][nx] = 0
                        q.append([ny,nx])

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                graph[i][j] = 0
                bfs(i,j)
                cnt += 1
    print(cnt)


