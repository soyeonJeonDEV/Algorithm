#수 정렬하기2
import sys
input = sys.stdin.readline


n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a = sorted(a)

for i in a:
    print(i)