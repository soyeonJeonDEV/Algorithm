# 운동
import sys

input = sys.stdin.readline
inf = sys.maxsize
v,e = map(int,input().split())
graph = [[inf]*(v+1) for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a][b] = c


for k in range(1, v+1):
    for i in range(1,v+1):
        for j in range(1, v+1):
            if i==j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[k][j] + graph[i][k])
result = inf

for i in range(1,v):
    for j in range(i,v+1):
        if i != j:
            result = min(graph[i][j]+graph[j][i], result)

if result == inf:
    print(-1)
else:
    print(result)