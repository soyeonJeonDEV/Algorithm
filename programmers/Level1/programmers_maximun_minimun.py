#https://programmers.co.kr/learn/courses/30/lessons/12940
#최대 공약수와 최소 공배수

import math
def solution(n,m):
    return [math.gcd(n,m), (n*m)/math.gcd(n,m)]

'''
#풀어쓰기
def gcdlcm(a,b):
    c,d = max(a,b), min(a,b)
    t = 1
    while t > 0:
        t = c % d
        c,d = d,t
    answer = [c, int(a*b/c)]

    return answer 
'''