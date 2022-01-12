#https://www.acmicpc.net/problem/10448
#유레카 이론

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]


t = [int((i*(i+1))/2)for i in range(1,45)]

dp = [0 for _ in range(1001)]

#미리 1000이하의 유레카 값을 다 구한다.
for i in t:
    for j in t:
        for k in t:
            if i+j+k <= 1000:
                dp[i+j+k] = 1
for i in arr:
    print(dp[i])
