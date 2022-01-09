#https://www.acmicpc.net/problem/13549
#숨바꼭질 3

from collections import deque

n,k = map(int, input().split())
ch = [(-1) for _ in range(100001)]
def bfs(start):
    q = deque()
    q.append(n)

    ch[start] = 0

    while q:
        x = q.popleft()

        #2*x는 cost가 가장 작으므로 첫번째
        #x-1이 x+1보다 먼저 하는 것은 -1 이동후 *2 이동을 했을 때, 먼저 도착하는 경우가 있어서
        for new_x in (2*x, x-1, x+1):
            if 0<=new_x<100001 and ch[new_x] == -1:
                if new_x == 2*x:
                    ch[new_x] = ch[x]
                    q.append(new_x)
                else:
                    ch[new_x] = ch[x] + 1
                    q.append(new_x)
    
                
bfs(n)
print(ch[k])