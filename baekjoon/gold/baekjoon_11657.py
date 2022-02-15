# 타임머신
# 벨만-포드의 알고리즘 사용
# 다익스트라와의 차이점은 매 반복마다 모든 간선을 확인한다는 것
# 벨만-포드 알고리즘은 다익스트라에 비해 느리므로 가중치가 음수인 경우에만 사용하는 게 좋다.


import sys

input = sys.stdin.readline
inf = sys.maxsize

N,M = map(int,input().split())
graph = []
dp = [inf] *(N+1)
for _ in range(M):
    a,b,d = map(int,input().split())
    graph.append((a,b,d))

def bf(start):
    dp[start] = 0
    for i in range(N): # 정점 수 만큼 반복
        for j in range(M): # 매 반복마다 모든 간선 확인
            node = graph[j][0]
            next_node = graph[j][1]
            wei = graph[j][2]
            # 현재 간선을 걸쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dp[node] != inf and dp[next_node] > dp[node] + wei:
                dp[next_node] = dp[node] + wei
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == N-1:
                    return True
    return False

# 벨만-포드 알고리즘 수행
negative_cycle = bf(1)

if negative_cycle:
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, N+1):
        if dp[i] == inf:
            print(-1)
        else:
            print(dp[i])
