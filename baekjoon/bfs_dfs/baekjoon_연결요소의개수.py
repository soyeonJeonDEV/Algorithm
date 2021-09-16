#연결요소의 개수
#https://www.acmicpc.net/problem/11724
import sys
sys.setrecursionlimit(10000)

n,m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
graph[0] = [0,0]
count = 0

for _ in range(m):
  u,v = map(int,sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)
  graph[u].sort()
  graph[v].sort()

def dfs(graph,u,visited):
  visited[u] = True
  
  for i in graph[u]:
    if not visited[i]:
      dfs(graph,i,visited)


for i in range(1,n+1):
  if not visited[i]:
    count += 1
    dfs(graph,i,visited)


print(count)