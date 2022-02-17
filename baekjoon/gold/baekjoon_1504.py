# 특정한 최단 경로

import sys, heapq
input = sys.stdin.readline

INF = sys.maxsize
N, E = map(int,input().split())
heap = []
graph= [[] for _ in range(N+1)]

def solution(start):
    # 1, v1, v2의 dp를 구해야 하므로 solution 안에서 초기화
    dp = [INF] * (N+1)
    dp[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        w, now = heapq.heappop(heap)

        for next_node,wei in graph[now]:
            next_wei = wei+w
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap,(next_wei, next_node))

    return dp


for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

v1,v2 = map(int,input().split())

#v1,v2 정점을 지나야 하므로 1 -> v1 -> v2 -> N 까지의 최단길이나 1 -> v2 -> v1 -> N 까지의 최단길이를 구한다.
one = solution(1)
v1_ = solution(v1)
v2_ = solution(v2)
cnt = min(one[v1] + v1_[v2] +v2_[N], one[v2] + v2_[v1] + v1_[N])
print(cnt if cnt < INF else -1)

