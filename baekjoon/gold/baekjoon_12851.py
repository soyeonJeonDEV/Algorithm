#https://www.acmicpc.net/problem/12851
#숨바꼭질2
from collections import deque
n,k = map(int,input().split())
#[[시간, 경우의 수]]
ch=[[-1,0] for i in range(100001)]
def bfs(n):
    q = deque()
    q.append(n)
    ch[n][0] = 0 # 시작 시점 0초
    ch[n][1] = 1 # 시작 지점에 한번 들렀으니 경우의 수 1

    while q:
        x = q.popleft()

        for i in (x+1, x-1, x*2): # 움직이는 세가지 방법
            if 0<= i < 100001: # 조건
                if ch[i][0] == -1: # 처음 방문한 곳이라면
                    ch[i][0] = ch[x][0] + 1 # 이전 방문한 x 값의 시간에서 1초 더한다.
                    ch[i][1] = ch[x][1] # 처음 방문한 곳이므로 경우의 수
                    q.append(i)
                elif ch[i][0] == ch[x][0] + 1: # 다시 방문한 곳이라면(방문한 거리와 시간이 같다면)
                    ch[i][1] += ch[x][1] # 경우의 수를 하나 늘린다.
        

bfs(n)
print(ch[k][0]) # 걸린 시간
print(ch[k][1]) # 경우의 수

