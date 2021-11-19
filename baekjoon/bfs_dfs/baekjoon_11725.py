#https://www.acmicpc.net/problem/11725
#트리의 부모 찾기
import sys
input = sys.stdin.readline
#기본적으로 반복은 1000회로 되어있기 때문에 , 반복제한을 늘려줌
sys.setrecursionlimit(10**9)

n = int(input())
trees = [[] for _ in range(n+1)]
trees[0] = 0
for i in range(1,n):
    x,y = map(int,input().split())
    trees[x].append(y)
    trees[y].append(x)

answer = []
parent = [0 for _ in range(n+1)]

m = 0

def dfs(x):
    for i in trees[x]:         
        if parent[i] == 0:
            parent[i] = x
            dfs(i)

dfs(1)

for i in range(2,n+1):
    print(parent[i])