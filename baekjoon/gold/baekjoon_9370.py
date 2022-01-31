# 미확인 도착지

# s지점에서 출발 최단거리 도착, g와 h 사이에 있는 교차로 통과

import heapq, sys
input = sys.stdin.readline
inf = sys.maxsize

T = int(input())

def solution(start):
        dp = [inf]*(n+1)
        dp[start] = 0
        heapq.heappush(heap,(0,start))

        while heap:
            w, now = heapq.heappop(heap)

            for next_node, wei in graph[now]:
                next_wei = w+wei
                if next_wei < dp[next_node]:
                    dp[next_node] = next_wei
                    heapq.heappush(heap,(next_wei, next_node))
        return dp

for _ in range(T):
    # 교차로, 도로, 목적지 후보
    n,m,t = map(int,input().split())
    # 예술가들의 출발지, 교차로
    s,g,h = map(int,input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    des = []
    heap = []

    for i in range(t):
        des.append(int(input()))


    s_ = solution(s)
    g_ = solution(g)
    h_ = solution(h)
    ans = []

    for i in des:
        if s_[g] + g_[h] + h_[i] == s_[i] or s_[h] + h_[g] + g_[i] == s_[i]:
            ans.append(i)

    ans.sort()
    print(*ans)


    
