#x만큼 간격이 있는 n개의 숫자
#https://programmers.co.kr/learn/courses/30/lessons/12954
'''
#내가 푼 풀이
https://programmers.co.kr/learn/courses/30/lessons/12954
'''
#더 좋은 풀이
def solution(x, n):
    return [i*x + x for i in range(n)]