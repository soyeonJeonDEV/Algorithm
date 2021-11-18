#https://www.acmicpc.net/problem/2644
#촌수 계산

def dfs(c):
    global count
    if count > 0:
        return 
    if c == r2:
         count = visited.count(True) - 1
         return
    for i in trees[c]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
            visited[i] = False

    return
            

n = int(input())

r1,r2 = map(int,input().split())
tree = int(input())
trees = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
trees[0] = [0,0]
count = -1

for i in range(1, tree+1):
    a,b = map(int,(input().split()))
    trees[a].append(b)
    trees[b].append(a)

visited[r1] = True
dfs(r1)

print(count)
