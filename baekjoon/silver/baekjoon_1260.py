#https://www.acmicpc.net/problem/1260
#DFS와 BFS
from collections import deque

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[x].sort()
    graph[y].append(x)
    graph[y].sort()

visited = [False for _ in range(n+1)]
visited[v] = True
def dfs(num):
    print(num, end=" ")
    for i in graph[num]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

def bfs(num):
    q = deque()
    q.append((num))
    print(num,end=" ")
    while q:
        v_num = q.popleft()
        for i in graph[v_num]:
            if not visited[i]:
                visited[i] = True
                q.append((i))
                print(i,end=" ")
                
visited = [False for _ in range(n+1)]
visited[v] = True
dfs(v)
print("")
visited = [False for _ in range(n+1)]
visited[v] = True
bfs(v)

