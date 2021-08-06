#약수의 개수와 덧셈
#https://programmers.co.kr/learn/courses/30/lessons/77884
'''
#내가 푼 풀이
def solution(left, right):    
    sum = 0
    while left <= right:
        divisor = []
        for i in range(1,left+1):
            if left%i == 0:
                divisor.append(i)
        if len(divisor)%2 == 0:
            sum += left
        else:
            sum -= left
        left += 1
    return sum
'''
#더 좋은 풀이
#제곱수는 약수의 개수가 홀수
def solution(left, right):    
    sum = 0
    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:
            sum -= i
        else:
            sum += i
    return sum