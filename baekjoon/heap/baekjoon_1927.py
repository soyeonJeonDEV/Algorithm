#최소 힙
#https://www.acmicpc.net/problem/1927
import heapq

n = int(input())
heap = []

for i in range(n):
    temp = int(input())
    if temp == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,temp)