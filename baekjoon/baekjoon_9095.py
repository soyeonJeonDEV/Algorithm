#https://www.acmicpc.net/problem/9095
#1,2,3 더하기

t = int(input())

dp = [0 for _ in range(12)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

arr = [int(input()) for _ in range(t)]

for i in arr:
  for j in range(4,len(dp)):
    dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
  print(dp[i])
