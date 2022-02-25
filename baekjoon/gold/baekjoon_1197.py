# 최소 스패닝 트리
# kruskal
# 1. 간선들을 정렬
# 2. 간선이 있는 두 정점의 root를 찾는다.
# 3. 다르다면 하나의 root를 바꾸어 연결시켜준다.

# prim
# 1. 임이의 정점을 선택
# 2. 해당 정점에서 갈 수 있는 간선을 minheap에 넣는다.
# 3. 최소값을 뽑아 해당 정점을 방문 안했다면 선택한다.

# 간선이 적으면 kruskal, 많으면 prim

# import heapq

v,e = map(int,input().split())
# graph = [[] for _ in range(v+1)]

# for _ in range(e):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))
#     graph[b].append((a,c))

# heap = []
# dist = 0
# cnt = 0

# vi = [False for _ in range(v+1)]
# heapq.heappush(heap,(0,1)) # 가중치, 노드

# while heap:
#     if cnt == v:
#         break

#     wei, now = heapq.heappop(heap)

#     if not vi[now]:
#         vi[now] = True
#         dist += wei
#         cnt += 1
#         for next_node, w in graph[now]:
#             heapq.heappush(heap,(w,next_node))

# print(dist)

# vroot = [i for i in range(v+1)]
# graph = []
# for _ in range(e):
#     graph.append(list(map(int,input().split())))

# graph.sort(key=lambda x:x[2])

# def find(x):
#     if x != vroot[x]:
#         vroot[x] = find(vroot[x])
#     return vroot[x]

# answer = 0
# for start,end,wei in graph:
#     sroot = find(start)
#     eroot = find(end)
#     if sroot != eroot:
#         if sroot > eroot:
#             vroot[sroot] = eroot
#         else:
#             vroot[eroot] = sroot
#         answer += wei

# print(answer)


graph = []
root = [i for i in range(v+1)]
for _ in range(e):
    a,b,w = map(int,input().split())
    graph.append((w,a,b))
graph.sort()

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        root[b] = a
    else:
        root[a] = b
answer =0
for w, a, b in graph:
    if find(a) != find(b):
        union(a,b)
        answer += w

print(answer)