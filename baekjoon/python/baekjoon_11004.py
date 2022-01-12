#https://www.acmicpc.net/problem/11004
#k번째의 수
n,k = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a)
print(a[k-1])