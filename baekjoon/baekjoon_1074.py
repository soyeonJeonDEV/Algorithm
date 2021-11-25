#https://www.acmicpc.net/problem/1074
#Z
# 답보고 이해
n,r,c = map(int,input().split())

#4사분면 찾는 함수
def find(r,c):
    if 0<= r < 2**(n-1) and 0 <= c < 2**(n-1):
        return 1
    elif 0<= r < 2**(n-1) and 2**(n-1) <= c < 2**n:
        return 2
    elif 2**(n-1) <= r < 2**n and 0<= c < 2**(n-1):
        return 3
    else:
        return 4

#해당 분면에 좌표값 재배치
def reallocate():
    global r,c,n

    if res == 2:
        c -= 2**(n-1)
    elif res == 3:
        r -= 2**(n-1)
    elif res == 4:
        r -= 2**(n-1)
        c -= 2**(n-1)
    n -= 1

ans = 0
while True:
    if n <= 0:
        break
    res = find(r,c)
    #해당 분면에 시작값 ans에 더하기
    ans = ans + (res -1)*(4**(n-1))
    reallocate()

print(ans)