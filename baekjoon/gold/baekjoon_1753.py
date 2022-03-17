# 최단 경로

import sys
import heapq

# input = sys.stdin.readline
# INF = sys.maxsize
# V,E = map(int,input().split())
# #시작점 k
# K = int(input())
# #가중치 테이블 dp
# dp = [INF]*(V+1)
# heap = []
# graph = [[] for _ in range(V+1)]

# def Dijkstra(start):
#     # 가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
#     dp[start] = 0
#     heapq.heappush(heap, (0, start))

#     #힙에 원소가 없을 때 까지 반복.
#     while heap:
#         wei, now = heapq.heappop(heap)

#         # 현재 테이블과 비교하여 불필요한 (더 가중치가 큰) 튜플이면 무시.
#         if dp[now] < wei:
#             continue

#         for w, next_node in graph[now]:
#             # 현재 정점 까지의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 W = 다음 노트까지의 가중치(next_wei)
#             next_wei = w + wei
#             # 다음 노드까지의 가중치(next_wei)가 현재 기록된 값보다 작으면 조건 성립.
#             if next_wei < dp[next_node]:
#                 # 계산했던 next_wei를 가중치 테이블에 업데이트
#                 dp[next_node] = next_wei
#                 # 다음 점까지의 가중치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입.
#                 heapq.heappush(heap, (next_wei, next_node))
# # 초기화
# for _ in range(E):
#     u,v,w = map(int,input().split())
#     #(가중치, 목적지 노드) 형태로 저장
#     graph[u].append((w,v))

# Dijkstra(K)
# for i in range(1,V+1):
#     print("INF" if dp[i] == INF else dp[i])

inf = sys.maxsize
v,e = map(int,input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
dp = [inf]*(v+1)

for _ in range(e):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

heap = []

def solution(start):
    dp[start] = 0

    heapq.heappush(heap,(0,start))

    while heap:
        w, now = heapq.heappop(heap)

        for next_node, wei in graph[now]:
            next_wei = wei+w
            if dp[next_node] > next_wei:
                dp[next_node] = next_wei
                heapq.heappush(heap,(next_wei,next_node))

solution(k)

for i in range(1,len(dp)):
    if dp[i] == inf:
        print('INF')
    else:
        print(dp[i])
    
