#보석 도둑

import heapq 

n,k = map(int,input().split())
jewel = [list(map(int,input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
#q보석의 무게, 배낭의 무게 순서대로 정렬
jewel.sort()
bag.sort()

heap =[]
result = 0

# 가방 무게 작은 거부터
for k in bag:
    # 보석이 있고, 보석 무게가 가장 작은게 가방 무게 보다 작다면
    while jewel and k>= jewel[0][0]:
        # heap에다가 가격을 큰 순서대로 집어넣어라
        heapq.heappush(heap, -jewel[0][1])
        # 젤 앞에 있는 보석을 배열에서 제거해라
        heapq.heappop(jewel)
    # 조건이 충족돼 heap에 들어온다면(가격이 큰 순서대로)
    if heap:
        # 결과에 heap 안에 들어있는 값을 더해라
        result += heapq.heappop(heap)
    # 보석이 더이상 없다면 멈춰라
    elif not jewel:
        break

#우선순위 큐로 heap 안에 집어넣었기 떄문에 -를 붙여야 양수로 나온다.
print(-result)