#https://www.acmicpc.net/problem/11724
#연결 요소의 개수

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = 0

def dfs(st):
    visited[st] = True
    for i in graph[st]:
        if visited[i] == False:
            dfs(i)

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)