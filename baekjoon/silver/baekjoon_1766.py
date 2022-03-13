#문제집 
#https://www.acmicpc.net/problem/1766
'''
위상정렬
- 사이클이 없는 방향그래프에서 순서가 정해져 있는 작업을 차례로 수행
해야 할 때, 순서를 정해주는 알고리즘
1. 진입차수가 0인 정점을 큐에 삽입
2. 큐에서 원소를 꺼내 해당 원소와 연결된 간선을 모두 제거
3. 제거한 후에 진입차수가 0인 정점을 큐에 삽입
4. 이후 2~3의과정을 반벅

모든 원소를 방문하지 건에 큐가 비게 된다면 사이클이 존재하는 그래프
사이클이 존재하는 그래프는 위상정렬을 적용할 수 없다.

우선순위 큐 사용

'''


import heapq

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)] # 진입차수
answer = []
heap = []

for i in range(m):
    frist, second = map(int,input().split())
    graph[frist].append(second) 
    inDegree[second] += 1 # second는 선수문제가 존재함으로 진입 차수 + 1

for i in range(1,n+1):
    if inDegree[i] == 0: #집입차수가 0이라면 선수문제
        heapq.heappush(heap,i)


while heap:
    temp = heapq.heappop(heap)
    answer.append(temp)

    for i in graph[temp]: # 두번째 문제
        inDegree[i] -= 1 # 1을 빼준다.
        if inDegree[i] == 0: #0이라면 다음 풀 문제
            heapq.heappush(heap,i)

print("".join(map(str,answer)))