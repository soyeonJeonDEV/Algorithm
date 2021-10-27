#https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
#소수찾기
from itertools import permutations  
def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        nums = list(permutations(numbers,i))
        for j in range(len(nums)):
            n = int(''.join(nums[j]))
            flag = True
            if n == 0 or n == 1:
                flag = False
            else:
                for k in range(2, n):
                    if n%k == 0:
                        flag = False
                        break
            if flag:
                answer.append(n)
    answer = set(answer)
    return len(answer)