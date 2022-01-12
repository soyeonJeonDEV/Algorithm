#알파벳
#https://www.acmicpc.net/problem/1987
import sys

def bfs(a,b):
    global answer
    q = set()
    q.add((a,b,graph[a][b]))

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        print(q)
        y,x,alpha = q.pop()
  
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<c and 0<=ny<r:
                if graph[ny][nx] not in alpha:
                    q.add((ny,nx,alpha + graph[ny][nx]))
                    answer = max(answer,len(alpha)+1)


input = sys.stdin.readline
r,c = map(int,input().split())
graph = [list(map(str, input()))for _ in range(r)]
answer = 1
bfs(0,0)
print(answer)