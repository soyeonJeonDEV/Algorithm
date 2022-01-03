#https://www.acmicpc.net/problem/1987
#알파벳
"""
1. 말은 상하좌우로 이동할 수 있다.
2. 지금까지 지나온 알파벳의 칸으로는 이동할 수 없다.
"""

r,c = map(int,input().split())
graph = [list(map(str,input())) for _ in range(r)]
#말이 지나는 칸은 좌측상단의 칸도 포함된다.
answer = 1

def bfs(a,b):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    #set함수를 통해 같은 변수가 들어오지 않도록 한다.(시간 단축)
    q = set()
    #set함수는 append가 아니라 add를 사용
    #좌표값과 현재 칸의 알파벳을 집어넣는다.
    q.add((a,b,graph[a][b]))
    global answer

    while q:
        y,x, location= q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<c and 0<=ny<r:
                #지금까지 지나온 알파벳들 안에 graph[ny][nx] 알파벳이 없으면
                if graph[ny][nx] not in location:
                    #q에 이동한 좌표값과 지금까지 지나온 알파벳과 이동한 칸의 알파벳을 더한 값을 집어넣는다
                    q.add((ny,nx,location + graph[ny][nx]))
                    #answer 값과 아직 location값이 이동전 location값이므로 +1을 해줘 두 개의 값을 비교 후 큰 값을 answer에 집어넣는다.
                    answer = max(answer, len(location)+1)
bfs(0,0)
print(answer)   
