# 스타트링크
# F층 건물, 스타트링크 위치 G, 현재 위치 S, UP U, DOWN D

from collections import deque

F,S,G,U,D = map(int,input().split())

def bfs():
    q = deque()
    q.append(S)
    visit = [0]*(F + 1)
    visit[S] = 1

    while q:
        x = q.popleft()
        if x == G:
            print(visit[G] - 1)
            return 

        up = x + U
        down = x - D

        if up <= F and not visit[up]:
            q.append(up)
            visit[up] = visit[x] + 1
        
        if down > 0 and not visit[down]:
            q.append(down)
            visit[down] = visit[x] + 1

    else:
        print('use the stairs')
        return 

bfs()