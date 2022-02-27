# 노드사이의 거리
from collections import deque

n,m = map(int,input().split())
graph =[[] for _ in range(n+1)]

def bfs(a,b):
    q = deque()
    q.append((a,b))

    while q:
        x,y = q.popleft()
        if 


for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

for _ in range(m):
    a,b = map(int,input())
    bfs(a,b)
