# 벽 부수고 이동하기

from collections import deque
import copy


n, m = map(int,input().split())

graph = [list(map(int,input())) for _ in range(n)]

# def bfs():
#     dx = [-1,0,1,0]
#     dy = [0,1,0,-1]
#     q = deque()
#     q.append((0,0))
#     temp = copy.deepcopy(graph)
    
#     while q:
#         y,x = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0<=nx<m and 0<=ny<n:
#                 if temp[ny][nx] == 0:
#                     temp[ny][nx] = temp[y][x] + 1
#                     q.append((ny,nx))

#     global answer
#     cnt = temp[-1][-1]
#     if cnt != 0:
#         answer = min(cnt, answer)


# answer = float('inf')
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1:
#             graph[i][j] = 0
#             bfs()
#             graph[i][j] = 1

# if answer == float('inf'):
#     print(-1)
# else:
#     print(answer+1)

def bfs():
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    q = deque()
    q.append([0,0,1])
    visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visit[0][0][1] = 1 # 벽을 한 번 부술 수 있는 상태에서 시작
    
    while q:
        x,y,w = q.popleft()
        if x == m-1 and y == n-1:
            return visit[y][x][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx<m and 0<=ny<n:
                if graph[ny][nx] == 1 and w == 1: # 벽을 만나고 벽을 한 번 부술 수 있는 경우
                    visit[ny][nx][0] = visit[y][x][w] + 1
                    q.append([ny,nx,0])
                elif graph[ny][nx] == 0 and visit[ny][nx][w] == 0: # 벽이 없고 방문 한 적이 없는 경우
                    visit[ny][nx][w] = visit[y][x][w] + 1
    return -1

print(bfs())