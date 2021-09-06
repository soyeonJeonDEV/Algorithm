#짝지어 제거하기
#https://programmers.co.kr/learn/courses/30/lessons/12973
#내가 푼 풀이 : 런타임 에러로 인한 오류
'''
def solution(s):
    basket = []
    for i in s:
        basket.append(i)
        for j in range(len(basket)):
            if len(basket) >= 2 and basket[j] == basket[j-1]:
                basket.pop(-1)
                basket.pop(-1)
            

    return 1 if basket == []  else 0
'''
def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else :
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
    return 0 if stack else 1