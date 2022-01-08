#https://www.acmicpc.net/problem/16953
#A -> B
from collections import deque

a,b = map(int,input().split())
def bfs(a, cnt):
    q = deque()
    q.append((a, cnt))
    while q:
        x, cnt = q.popleft()
        if x == b:
            return cnt    
        plus_x = int(str(x) + '1')
        multi_x = x*2
        if multi_x <= b:
            q.append((multi_x, cnt+1))
        if plus_x <= b:
            q.append((plus_x, cnt+1))
    return -1

print(bfs(a,1))
