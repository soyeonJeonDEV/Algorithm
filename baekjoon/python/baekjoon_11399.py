#https://www.acmicpc.net/problem/11399
#ATM

n = int(input())

hour = list(map(int,input().split()))

hour.sort()

m = 0
sum = 0


for i in range(n):
  m += hour[i]
  sum += m
  
print(sum)