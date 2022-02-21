# 보물섬
# 상하좌우 육지로만 이동 가능, 한 칸 이동하는데 +1
# 보물은 가장 먼 거리에 묻혀있고, 최대 거리를 구해라
# 완전탐색?
# 좌표 하나를 선택해서 최대거리를 구하고 answer 저장
# 다른 좌표를 하나 선택해서 최대거리를 구하고 answer 저장
# 모든 L 좌표에서 최대거리를 구하고 가장 많이 걸리는 시간을 답으로 도출


from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline())) for _ in range(n)]

def bfs(a,b):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visited = [[False]*m for _ in range(n)]
    visited[a][b] = True
    dist = [[0]*m for _ in range(n)]

    q = deque()
    q.append((a,b))

    global answer

    while q:
        y,x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n:
                if not visited[ny][nx] and graph[ny][nx] == 'L':
                    visited[ny][nx] = True
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny,nx))

    cnt = max(map(max, dist))
    answer = max(cnt, answer)
        
answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':  
            bfs(i,j)

print(answer)