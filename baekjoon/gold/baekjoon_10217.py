# KCM Travel
# 모든 경우의 수 확인
# dp 이용

import sys
input = sys.stdin.readline
inf = float('inf')
# 테스트 케이스의 수
T = int(input())


for _ in range(T):
    # 공항의 수, 비용, 티켓 정보
    n,m,k = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        # 출발, 도착, 비용, 소요시간
        u,v,c,d = map(int,input().split())
        graph[u].append((v,c,d))

    # 열 : 비용 행 : n 까지 갈 때
    dp = [[inf]*(m+1) for _ in range(n+1)]
    dp[1][0] = 0 # 1 -> 1로 갔을 때 비용 0, 시간 0

    for cost in range(m+1):
        for node in range(n+1):
            if dp[node][cost] == inf: continue
            time = dp[node][cost] # cost 비용으로 node에 도착했을 때 소요시간
            for dv,dc,dd in graph[node]: # node에서 출발하는 모든 경우의 수
                if dc + cost > m: # 비용이 초과될 경우
                    continue
                dp[dv][dc+cost] = min(dp[dv][dc+cost], time+dd) 
    result = min(dp[n])

    if result == inf:
        print("Poor KCM")
    else:
        print(result)
