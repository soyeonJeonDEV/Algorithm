#https://www.acmicpc.net/problem/15652
#N과M 4
from itertools import combinations_with_replacement
n,m = map(int,input().split()) 
num = [str(i) for i in range(1,n+1)]
print('\n'.join(list(map(' '.join,combinations_with_replacement(num,m) ))))