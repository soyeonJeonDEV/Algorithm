#https://programmers.co.kr/learn/courses/30/lessons/12978
#배달
import heapq
def solution(N, road, K):
    graph = [[ ] for _ in range(N+1)]
    visited = [False] * (N+1)
    start = 1
    distance = [float('inf')] * (N+1)
    cnt = 0
    
    for i in road:
        a,b,c = i[0],i[1],i[2]
        graph[a].append([b,c])
        graph[b].append([a,c])
        
    heap(start,distance,graph)

    for i in range(1, len(distance)):
        if distance[i] <= K:
            cnt += 1
            
    return cnt


def heap(start, distance,graph):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))