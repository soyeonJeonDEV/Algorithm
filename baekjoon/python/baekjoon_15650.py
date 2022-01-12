#https://www.acmicpc.net/problem/15650
#N과M 2

from itertools import combinations

n,m = map(int, input().split())
num = [str(i) for i in range(1,n+1)]

print('\n'.join(list(map(' '.join, combinations(num,m)))))