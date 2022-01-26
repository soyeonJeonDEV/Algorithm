#연구소
#https://www.acmicpc.net/problem/14502

# 1. 빈칸, 벽으로 이루어져있다.
# 2. 바이러스는 상하좌우로 인접한 빈칸으로 퍼져나간다. 
# 3. 벽의 개수는 3개
# 4. 0은 빈칸, 1은 벽, 2는 바이러스
# 5. 0의 최대 크기를 구한다.
from collections import deque
import copy,sys

input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

def bfs():
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    q = deque()
    temp_graph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i,j))
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = 2
                    q.append((nx,ny))

    cnt = 0
    global answer 

    for i in temp_graph:
        cnt += i.count(0)
    answer = max(cnt, answer)

def wall(cnt):
    if cnt == 3:
        bfs()
        return 
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt+1)
                graph[i][j] = 0


answer = 0 
wall(0)
print(answer)
