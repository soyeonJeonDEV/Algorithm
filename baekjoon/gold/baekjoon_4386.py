# 별자리 만들기
import math

n = int(input())
parent = [i for i in range(n+1)]
star =[]
edge = []
result = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(n):
    x,y = map(float,input().split())
    star.append((x,y))

for i in range(n-1):
    for j in range(i+1, n):
        edge.append((math.sqrt((star[i][0] - star[j][0])**2 +(star[i][1] - star[j][1])**2), i,j))


edge.sort()

for e in edge:
    cost, x, y = e
    if find(x) != find(y):
        union(x,y)
        result += cost

print(round(result,2))
    