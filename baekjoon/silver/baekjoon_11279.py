# 최대 힙

import sys, heapq
n = int(input())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(heap,-x)
    elif x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
