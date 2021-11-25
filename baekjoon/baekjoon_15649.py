#https://www.acmicpc.net/problem/15649
#N과M
from itertools import permutations

n,m = map(int,input().split())
num = [str(i) for i in range(1,n+1)]

print("\n".join(list(map(' '.join, permutations(num,m)))))