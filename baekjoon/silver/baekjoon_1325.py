#효율적인 해킹

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

answer = [0 for _ in range(n+1)]
def dfs(num):
    global cnt 
    if not graph[num]:
        return
    for i in graph[num]:
        if chk[i] == 0 and graph[i]:
            chk[i] = 1
            cnt += 1
            dfs(i)

for i in range(1,n+1):
    cnt = 0
    chk = [0 for _ in range(n+1)]
    chk[i] = 1
    dfs(i)
    answer[i] = cnt

answer = list(enumerate(answer))
a = sorted(answer, key=lambda x:x[1], reverse=True)
for i in a:
    if i[1] != 0:
        print(i[0],end=" ")
