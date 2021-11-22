#https://www.acmicpc.net/problem/1655
#가운데를 말해요
import sys

input = sys.stdin.readline()

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
    if i == 0: 
        print(num[i])
        continue
    else:
        num = sorted(num)
        if len(num) % 2 == 0:
            print(num[len(num)//2-1])
        else:
            print(num[len(num)//2])

