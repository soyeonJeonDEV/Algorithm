#미로 만들기
#다익스트라 알고리즘 사용
#모든 노선을 지나가면서 가장 먼저 도착지점에 도착한 경우가 가장 짧다.
#모든 경우의 수를 구할 경우 사용



from heapq import heappush, heappop

n = int(input())

maze = [list(map(int,input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def bfs():
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    heap = []
    heappush(heap,[0,0,0]) #바꾼 방의 개수, x, y
    visited[0][0] = 1

    while heap:
        a, x, y = heappop(heap)
        if x == n -1 and y == n - 1: # 도착지점이면
            print(a)
            return
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0 <=ny<n and not visited[nx][ny]:
                visited[nx][ny] = True

                if maze[nx][ny] == 0:
                    heappush(heap,[a+1,nx,ny]) # 0이라면 지나가고 a의 개수를 늘려 통과해라

                else:
                    heappush(heap[a,nx,ny])

