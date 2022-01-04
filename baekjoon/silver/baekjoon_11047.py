#https://www.acmicpc.net/problem/11047
#동전 0

n, k = map(int,input().split())

coin =[]
count = 0

for i in range(n):
  coin.append(int(input()))
  
coin.sort(reverse = True)

for i in coin:
  count += k//i
  k %= i
  if(k == 0):
    break
  
print(count)

