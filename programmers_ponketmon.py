#폰켓몬
#https://programmers.co.kr/learn/courses/30/lessons/1845?language=python3
#내가 푼 풀이
'''
def solution(nums):
    n = len(nums)
    sort = set(nums)
    if len(sort) >= (n/2):
        return n/2
    else:
        return len(sort)
'''
#좋은 풀이 방법
def solution(nums):
    return min(len(nums)/2, len(set(nums)))
  