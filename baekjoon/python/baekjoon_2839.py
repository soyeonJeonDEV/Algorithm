#https://www.acmicpc.net/problem/2839
#설탕배달
n = int(input())
box = 0

while True:
  if (n % 5) == 0:
    box += n//5
    print(box)
    break
  
  n -= 3
  box += 1
  if n < 0:
    print(-1)
    break  
    
  