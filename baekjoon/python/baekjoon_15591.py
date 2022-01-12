#MooTub
from collections import defaultdict, deque
N,Q = map(int,input().split())
map_dict = defaultdict(list)

def bfs(st,k,map_dict):
    queue = deque()
    queue.append((st, float('inf')))
    visit_list = [-1]*N
    visit_list[st] = 1
    count = 0

    while queue:
        pop_node, min_dist = queue.popleft()
        for next_n, dist in map_dict[pop_node]:
            if visit_list[next_n] == 1: continue
            if min_dist > dist:
                queue.append((next_n,dist))
                if dist >= k:count += 1
            else:
                queue.append((next_n,min_dist))
                if min_dist >= k: count += 1
            visit_list[next_n] = 1
    return count

for _ in range(N-1):
    p,q,r = map(int,input().split())
    map_dict[p-1].append((q-1,r))
    map_dict[q-1].append((p-1,r))

for _ in range(Q):
    k,v = map(int,input().split())
    print(bfs(v-1,k,map_dict))

print(map_dict)