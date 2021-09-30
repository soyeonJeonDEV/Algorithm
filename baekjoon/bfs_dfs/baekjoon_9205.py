#맥주마시면서 걸어가기
#https://www.acmicpc.net/problem/9205
from collections import deque

def bfs():
    q = deque()
    q.append(home_dir)
    while q:
        x,y = q.popleft()
        if abs(x-fes_dir[0]) + abs(y-fes_dir[1]) <= 1000:
            print("happy")
            return
        for i in range(conv):
            if not visited[i]:
                nx,ny = conv_dir[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    q.append([nx,ny])
                    visited[i] = 1
    print("sad")
    return

t_case = int(input())
for i in range(t_case):
    conv = int(input())
    home_dir = list(map(int,input().split()))
    conv_dir = [list(map(int,input().split())) for _ in range(conv)]
    fes_dir = list(map(int,input().split()))
    visited = [0 for i in range(conv+1)]
    bfs()