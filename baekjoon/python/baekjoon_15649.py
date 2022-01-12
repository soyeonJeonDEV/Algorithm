#https://www.acmicpc.net/problem/15649
#N과M
from itertools import permutations

n,m = map(int,input().split())
# num = [str(i) for i in range(1,n+1)]

# print("\n".join(list(map(' '.join, permutations(num,m)))))

rs = []
chk = [False] * (n+1)
def recur(num):
    if num == m:
        print(' '.join(map(str,rs)))
        return
    for i in range(1,n+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)
            chk[i] = False
            rs.pop()
recur(0)