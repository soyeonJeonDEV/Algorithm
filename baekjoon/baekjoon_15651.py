#https://www.acmicpc.net/problem/15651
#N과M 3

from itertools import product

n,m = map(int, input().split())
num = [str(i) for i in range(1,n+1)]

print('\n'.join(list(map(' '.join, product(num,repeat = m)))))