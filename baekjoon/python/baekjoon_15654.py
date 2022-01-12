#https://www.acmicpc.net/problem/15654
#N과 M
from itertools import permutations

n,m = map(int,input().split())
num = sorted(list(map(str, input().split())))

print('\n'.join(list(map(' '.join,permutations(num,m)))))