#가운데 글자 가져오기
#https://programmers.co.kr/learn/courses/30/lessons/12903
'''
#내가 푼 풀이
import math
def solution(s):
    answer = ''
    mid = math.floor(len(s)/2)
    if len(s) % 2 == 0:
        for i in range(1,-1,-1):
            answer += s[mid-i]
        return answer
    else:
        return s[mid]

'''
#보기 좋은 풀이
def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]