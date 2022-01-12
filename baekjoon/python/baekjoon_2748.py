#피보나치수2
#https://www.acmicpc.net/problem/2748

n = int(input())

dp = [0 for _ in range(91)]
dp[1] = 1

for i in range(2,n+1):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[n])