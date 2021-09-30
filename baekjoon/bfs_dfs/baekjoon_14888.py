#연산자끼어넣기
#https://www.acmicpc.net/problem/14888

import math
from itertools import permutations

n = int(input())
num = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())
min_,max_ = 1e9,-1e9

def dfs(i,res,add,sub,mul,div):
    global min_,max_
    if i == n:
        max_ = max(res,max_)
        min_ = min(res,min_)
        return
    else:
        if add:
            dfs(i+1, res+num[i], add -1, sub,mul,div)
        if sub:
            dfs(i+1, res-num[i],add,sub-1,mul,div)
        if mul:
            dfs(i+1, res*num[i],add,sub,mul-1,div)
        if div:
            dfs(i+1, int(res/num[i]),add,sub,mul,div-1)
dfs(1,num[0],add,sub,mul,div)
print(max_)
print(min_)