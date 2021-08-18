#124나라의 숫자
#https://programmers.co.kr/learn/courses/30/lessons/12899#
'''
def solution(n):
    result = ''
    while n > 0:
        if n % 3 == 1:
            result += '1'
            n //= 3
        elif n % 3 == 2:
            result += '2'
            n //= 3
        else:
            result += '4'
            n //= 3
            n -= 1
    #뒤집어서 return 
    return "".join(result[::-1])
'''
# 더 간단한 풀이
def change124(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer