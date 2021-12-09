#https://www.acmicpc.net/problem/1956
#운동

import math, sys
input = sys.stdin.readline


v,e = map(int,input().split())
tree = [[math.inf]*(v+1) for _ in range(v+1)]

for i in range(e):
    a,b,c = map(int,input().split())
    tree[a][b] = c

for i in range(1,v+1):
    tree[i][i] = 0

for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            tree[i][j] = min(tree[i][j], tree[i][k]+tree[k][j])

answer = math.inf
for i in range(1,v+1):
    for j in range(1,v+1):
        if i == j :
            continue
        if tree[i][j] != math.inf and tree[j][i] != math.inf:
            answer = min(answer, tree[i][j] + tree[j][i])

if answer == math.inf:
    print(-1)
else:
    print(answer)