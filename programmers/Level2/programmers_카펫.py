#https://programmers.co.kr/learn/courses/30/lessons/42842
#카펫
def solution(brown, yellow):
    n = brown+yellow
    temp = [i for i in range(n,2,-1) if n%i == 0 ]
    for i in range(n,2,-1):
        if n%i == 0:
            a = n//i
            if (a-2)*(i-2) == yellow:
                return [i,a]