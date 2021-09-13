#바이러스
#https://www.acmicpc.net/problem/2606

from collections import deque
n = int(input())
pair = int(input())

graph = [[] for _ in range(n+1)]
graph[0] = [0,0]
visited = [false for _ in range(n+1)]
count = 0

for _ in range(pair):
  start,end = map(int,input().split())

  graph[start].append(end)
  graph[end].append(start)


def dfs(graph,start,visited):
  global count
  visited[start] = True
  count += 1

  for i in graph[start]:
    if not visited[i]:
      dfs(graph,i,visited)

dfs(graph,1,visited)

print(count-1)