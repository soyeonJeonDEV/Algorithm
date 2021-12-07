#https://programmers.co.kr/learn/courses/30/lessons/12907
#거스름돈
#dp문제/ 답보고 이해

def solution(n, money):
    rest = [1] + [0]*n
    print(rest)
    for m in money:
        for i in range(m,n+1):
            if i >= m:
                rest[i] += rest[i-m]
                
    return rest[n] % 1000000007