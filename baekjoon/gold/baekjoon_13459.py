# 구슬탈출1

'''
Queue에 빨간 구슬의 (X, Y) 좌표, 파란 구슬의 (X, Y) 좌표를 모두 넣는다.
방문 여부를 확인할 check 배열을 4차원 배열로 선언한다. 배열의 인덱스는 [빨간 X좌표] [빨간 Y좌표] [파란 X좌표] [파란 Y좌표] 이다.
구슬을 굴릴 때, 구슬의 다음 위치가 벽(#)인지, 구슬의 현재 위치가 구멍(O)인지 확인한다.
구슬의 다음 위치가 벽이라면 앞으로 가지 못한다. 구슬의 현재 위치가 구멍이라면, 현재 구슬의 색이 무엇인지 판별한다.
만약 파란 구슬의 현재 위치가 구멍이라면 무시하고, 빨간 구슬의 현재 위치가 구멍이라면, 1을 출력하고 종료한다.
구슬을 굴리면서, 빨간 구슬의 이동 거리와 파란 구슬의 이동 거리를 카운트해야 한다.
구슬을 굴린 후, 빨간 구슬의 위치와 파란 구슬의 위치가 같다면, 이동 거리 비교를 통해 겹치지 않도록 처리해야 한다.
만약 구슬이 겹쳤다면, 굴릴 때 카운트했던 이동 거리가 더 긴 구슬의 위치를 한 칸 이전으로 되돌린다.
굴리는 과정이 10번을 넘어가면 그대로 종료하고, 0을 출력한다.
더 이상 갈 곳이 없을 때에는 BFS를 빠져나와서 0을 출력한다.

출처: https://rebas.kr/724 [PROJECT REBAS]
'''

n,m = map(int,input().split())

graph = [list(map(str,input())) for _ in range(n)]
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
queue = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def pos_init():
    rx,ry,bx,by = 0,0,0,0
    #파랑공, 빨강공 위치 저장
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'R':
                rx,ry = i,j
            elif graph[i][j] == 'B':
                bx,by = i,j
    
    queue.append((rx,ry,bx,by,1)) # 위치 정보와 depth
    visited[rx][ry][bx][by] = True # 방문 체크

def move(x,y,dx,dy):
    cnt = 0
    while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O': # 벽 그리고 구멍이 아닐동안
        x += dx # 현재 x 값에 x 축으로 값을 더한다.
        y += dy # y값에 y축으로 값을 더한다.
        cnt += 1 
    return x,y,cnt

def solve():
    pos_init() # 초기화
    while queue:
        rx,ry,bx,by, depth = queue.pop(0)
        if depth > 10: #실패 조건
            break
        for i in range(4):
            nrx,nry,rcnt = move(rx,ry,dx[i],dy[i]) # 새로운 x,y
            nbx,nby,bcnt = move(bx,by,dx[i],dy[i])
            if graph[nbx][nby] != 'O': # 파란공이 구멍에 없다면
                if graph[nrx][nry] == 'O': # 빨강공이 구멍에 있다면
                    print(depth) 
                    return
                if nrx == nbx and nry == nby : # 빨강공이랑 파란공이 같은 위치라면
                    if rcnt > bcnt: # cnt(즉, 이동한 거리) 를 비교해 빨강이 더 많으면
                        nrx -= dx[i] # 한칸 뒤로 이동
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]: # 방문하지 않았다면
                    visited[nrx][nry][nbx][nby] = True # 방문체크
                    queue.append((nrx,nry,nbx,nby,depth+1)) # 

    print(-1)

solve()