#https://programmers.co.kr/learn/courses/30/lessons/12980
#점프와 순간이동
def solution(n):
    cnt = 0
    if n > 1:
        while n != 0:
            if n % 2 == 0:
                n /= 2
            else:
                n -= 1
                cnt += 1
    else:
        cnt = 1
            
    return cnt