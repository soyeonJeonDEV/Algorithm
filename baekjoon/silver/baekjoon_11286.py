#절대값 힙
#https://www.acmicpc.net/problem/11286

import heapq,sys

n = int(input())
arr = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr,(abs(x),x))