#효율적인 해킹
#https://www.acmicpc.net/problem/1325

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
graph[0] = [0]
print(graph)
for i in range(m):
    start, end = map(int,input().split())
    graph[start].append(end)


print(graph)