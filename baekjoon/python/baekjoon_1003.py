#피보나치 함수
#https://www.acmicpc.net/problem/1003

cnt0 = [1,0]
cnt1 = [0,1]

t = int(input())

for i in range(2,41):
  cnt0.append(cnt0[i-1] + cnt0[i-2])
  cnt1.append(cnt1[i-1] + cnt1[i-2])

for _ in range(t):
  n = int(input())
  print(cnt0[n], cnt1[n])