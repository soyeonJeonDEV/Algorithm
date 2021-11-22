from collections import deque
def solution(m, n, board):
    answer = 0
    visited = [False * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                bfs(i,j)
                if cnt%2 == 0 and cnt >= 4: 
                    answer += cnt
    return answer
                
def bfs(a,b):
    cnt = 0
    q = deque()
    q.append([a,b])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    b = board[x][y]
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < m and 0<= ny < n:
                if board[nx][ny] == b and not visited[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = True
                    q.append([nx][ny])
    return cnt
        