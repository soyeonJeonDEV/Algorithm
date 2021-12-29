#https://www.acmicpc.net/problem/2606
#바이러스

computer = int(input())
pair = int(input())
net = [[] for _ in range(computer+1)]
visited = [False] * (computer+1)
visited[1] = True
answer = []

def dfs(num):
    for i in net[num]:
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            dfs(i)

# 양방향
for i in range(pair):
    n,m = map(int,input().split())
    net[n].append(m)
    net[m].append(n)

dfs(1)
print(len(answer))