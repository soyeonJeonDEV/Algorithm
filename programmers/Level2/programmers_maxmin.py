#최대값과 최소값
#https://programmers.co.kr/learn/courses/30/lessons/12939?language=python#

def solution(s):
    s = list(map(int,s.split()))
    s.sort()
    return "".join(str(s[0]) + ' ' + str(s[-1]))
            
    