#알파벳
#https://www.acmicpc.net/problem/1987
from collections import deque
import sys

def bfs(a,b):
    q = deque()
    q.append([a,b])
    alpha = deque()
    alpha.append(graph[a][b])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[a][b] = 1

    while q:

        y,x = q.popleft()
        al = alpha.popleft()
  
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            al = list(al)
            if 0<=nx<c and 0<=ny<r:
                if graph[ny][nx] in al:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny,nx])
                    alpha.append(al+graph[ny][nx])

    return max(map(max,visited))
input = sys.stdin.readline
r,c = map(int,input().split())
graph = [list(map(str, input()))for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]

print(bfs(0,0))