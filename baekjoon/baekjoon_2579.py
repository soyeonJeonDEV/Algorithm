#계단 오르기
#https://www.acmicpc.net/problem/2579

n = int(input())

scores= [0 for i in range(301)]
dp =[0 for _ in range(301)]

for i in range(n):
  scores[i] = int(input())

dp[0] = scores[0]
dp[1] = scores[0] + scores[1]
dp[2] = max(scores[1]+scores[2], scores[0]+scores[2])

for i in range(3,n):
  dp[i] = max(dp[i-3]+scores[i-1] + scores[i], dp[i-2] + scores[i])

print(dp[n-1])