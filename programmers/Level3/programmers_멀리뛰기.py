#https://programmers.co.kr/learn/courses/30/lessons/12914?language=python3
#멀리뛰기
def solution(n):
    a,b = 1,1
    
    for i in range(1,n+1):
        a,b = b, (a+b)%1234567
        
    return a