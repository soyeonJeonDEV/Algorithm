#https://www.acmicpc.net/problem/14501
#퇴사

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]

for i in range(n):
    dp[i+1] = max(dp[i], dp[i+1])
    if i + graph[i][0] <= n:
        dp[i+graph[i][0]] = max(dp[i+graph[i][0]],dp[i]+graph[i][1])

print(dp)