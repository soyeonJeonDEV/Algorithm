# 곱셈
# a = 10, b = 11, c = 12 일 떄
# 10^11 %12
# = ((10^5)%12 * (10^5) % 12 * 10) % 12
# = ((10^2)%12 *(10^2)%12 * 10)%12 * (10^2)%12 * (10^2)%12 * 10) % 12

import sys

a,b,c = map(int,sys.stdin.readline().split())

def solution(a,b): 
    if b == 1:
        return a%c
    #b가 1일 될때까지 solution에 들어간다.
    temp = solution(a,b//2)

    # b가 짝수일 때 
    if b % 2== 0:
        return temp * temp % c
    else:
        # 홀수일 떄
        return temp * temp * a % c

print(solution(a,b))