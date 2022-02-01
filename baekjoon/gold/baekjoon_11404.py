# 폴로이드
# 다익스트라 알고리즘으로 풀면 시간초과 발생
# 플로이드 와샬 알고리즘을 사용한다.
# 하나의 정점에서 모든 정점으로의 최단 거리를 구하는 알고리즘

import sys, heapq

input = sys.stdin.readline
inf = sys.maxsize

# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())
# 버스의 정보
# bus = [[] for _ in range(n+1)]
# for _ in range(m):
#     a,b,c = map(int,input().split())
#     bus[a].append((b,c))

# heap = []

# def solution(start):
#     dp = [inf] * (n+1)

#     dp[start] = 0
#     heapq.heappush(heap,(0, start))

#     while heap:
#         w, now = heapq.heappop(heap)

#         for next_node, wei in bus[now]:
#             next_wei = w + wei
#             if next_wei < dp[next_node]:
#                 dp[next_node] = next_wei
#                 heapq.heappush(heap,(next_wei, next_node))

#     return dp

# for i in range(1,n+1):
#     st = solution(i)
#     for j in range(1,n+1):
#         if st[j] == inf:
#             print(0, end =" ")
#         else:
#             print(st[j])

bus_cost =[[inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    # 같은 노선이 있기 때문
    bus_cost[a][b] = min(c, bus_cost[a][b])

# 플로이드-와샬 알고리즘
for k in range(1,n+1): # 경로 for문이 가장 상위 단계여야 누락되지 않는다.
    for i in range(1, n+1):
        for j in range(1,n+1):
            if i == j: # 자기 자신으로 오는 경우는 없다고 했으므로
                bus_cost[i][j] = 0
            else: # 경로 거치는 것 or 직접 가는 것 or 이전 경로들
                bus_cost[i][j] = min(bus_cost[i][j], bus_cost[i][k]+ bus_cost[k][j])

# 출력
for row in bus_cost[1:]:
    for col in row[1:]:
        if col == inf:
            print(0, end = " ")
        else:
            print(col, end =" ")
    print()

