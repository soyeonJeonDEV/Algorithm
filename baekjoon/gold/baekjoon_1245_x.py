# 농장 관리
# 주변에 인접한 값보다 크면 count x
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def dfs(a,b):
    # 인접한 값이니 8방향 전부 다
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    
    global trigger
    # 현재 위치 방문 값 True
    visited[a][b] = True

    # 8방향으로 인접 좌표값 체크
    for i in range(8):
        nx = a + dx[i]
        ny = b + dy[i]

        # 그래프 범위 안에서 
        if 0<=nx<n and 0<=ny<m:
            # 현재 좌표 값보다 인접한 좌표값이 더 크다면
            if graph[a][b]<graph[nx][ny]:
                # 현재 좌표가 봉우리가 아니므로 trigger = False
                trigger = False
            # 방문하지 않았고, 현재 좌표값과 인접한 좌표값이 같으면 
            if not visited[nx][ny] and graph[nx][ny] == graph[a][b]:
                dfs(nx,ny)

cnt = 0               
for i in range(n):
    for  j in range(m):
        # 방문하지 않은 좌표
        if not visited[i][j] and graph[i][j] > 0:
            # trigger = true로 초기화
            trigger = True
            # 차이가 1인 봉우리의 
            dfs(i,j)

            # trigger = true 라면 cnt + 1 해준다
            if trigger:
                cnt += 1


print(cnt)