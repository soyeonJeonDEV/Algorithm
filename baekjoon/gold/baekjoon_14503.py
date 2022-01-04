#https://www.acmicpc.net/problem/14503
#로봇청소기

"""
1. 아이디어
- while 문으로, 특정 조건 종료될 때까지 반복
- 4방향을 for문으로 탐색
- 더이상 탐색 불가능할 경우, 뒤로 한칸 후진
- 후진이 불가능하면 종료

2. 시간복잡도
- O(NM) : 50^2 = 2500 < 2억
-가능

3. 자료구조
- graph : int[][]
- 로봇청소기 위치, 방향, 전체 청소한 수
"""
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
y, x, d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
dy = [-1,0,1,0]
dx = [0,1,0,-1]

while 1:
    if graph[y][x] == 0:
        graph[y][x] = 2
        cnt += 1
    sw = False
    for i in range(1,5):
        #현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.
        #d-i : 내가 바라보는 위치에서 한칸씩 빼주면 왼쪽방향으로 간다.
        ny = y + dy[d-i]
        nx = x + dx[d-i]
        if 0<=ny<n and 0<=nx<m:
            #왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
            if graph[ny][nx] == 0:
                d = (d-i+4)%4
                y = ny
                x = nx
                sw = True
                break
    #4방향에 모두 있지 않은 경우
    if sw == False:         
        #뒤쪽 방향이 막혀있는지 확인
        ny = y - dy[d]
        nx = x - dx[d]
        if 0<=ny<n and 0<=nx<m:
            if graph[ny][nx] == 1:
                break 
            else:
                y = ny
                x = nx
        else:
            break


print(cnt)