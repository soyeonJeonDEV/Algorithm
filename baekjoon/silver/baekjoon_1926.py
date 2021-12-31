#https://www.acmicpc.net/problem/1926
#그림
"""
1. 아이디어
- 2중 for => 값 1 && 방문x ==> BFS
- BFS 돌면서 그림 개수 + 1, 최대값을 갱신

2. 시간 복잡도 
- BFS : O(V+E)
- V : 500 * 500
- E : 4 * 500 * 500
- V+E : 5 * 250000 = 100만 < 2억 >> 가능!

3. 자료구조
- 그래프 전체 지도 : int()[]
- 방문 bool[][]
- Queue(BFS)
"""

from collections import deque
import sys

input = sys.stdin.readline

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

# y를 먼저 돌고 x를 돈다
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
    
