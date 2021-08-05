#자릿수 더하기
#https://programmers.co.kr/learn/courses/30/lessons/12931
#내가 푼 풀이
def solution(n):
    return sum([int(i) for i in list(str(n))])
'''
#더 직관적인 풀이
def solution(n):
    return sum(list(map(int,str(n))))
'''