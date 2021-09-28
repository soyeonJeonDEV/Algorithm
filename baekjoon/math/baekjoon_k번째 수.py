#https://www.acmicpc.net/problem/11004
n,k = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a)
print(a[k-1])