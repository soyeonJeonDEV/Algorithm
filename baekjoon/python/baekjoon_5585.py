#https://www.acmicpc.net/problem/5585
#거스름돈
n = int(input())

coin = [500,100,50,10,5,1]
count = 0
cash = 1000 - n
for i in coin:
   count += cash//i
   cash %= i
   
   
print(count)