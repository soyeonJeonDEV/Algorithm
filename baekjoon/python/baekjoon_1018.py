#https://www.acmicpc.net/problem/1018
#체스판 다시 칠하기

n, m = map(int,input().split())

chess = [list(input()) for _ in range(n)]

for i in range(m):
    for j in range(n):
        if chess[i][j] == 'B':
           