#https://www.acmicpc.net/problem/2749
#피보나치 수 3
#시간초과

n = int(input())
a,b = 0,1

for i in range(n-1):
    a,b = b, (a+b)%1000000

print(b)
