#연속합
#https://www.acmicpc.net/problem/1912

n = int(input())
arr = list(map(int,input().split()))
dp = [arr[0]]
for i in range(len(arr)-1):
  #dp에 이전값과 현재값의 합과 현재값 중에 큰값을 dp에 넣는다.
  dp.append(max(dp[i] + arr[i+1], arr[i+1]))
#dp값중 최대값을 출력한다.
print(max(dp))
