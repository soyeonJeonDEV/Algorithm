#https://programmers.co.kr/learn/courses/30/lessons/12936
#줄서는 방법
#시간초과

from itertools import permutations
def solution(n, k):
    num = [i for i in range(1,n+1)]
    a = list(permutations(num,n))
    
    return a[k-1]