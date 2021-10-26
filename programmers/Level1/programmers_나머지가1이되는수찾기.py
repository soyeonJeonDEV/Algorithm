#https://programmers.co.kr/learn/courses/30/lessons/87389
#나머지가 1이 되는 수 찾기
'''
def solution(n):
    for i in range(1,n):
        if n%i == 1:
            answer = i
            break
            
    return answer
'''
# 더 좋은 코드
def solution(n):
    answer = min([x for x in range(1,n) if n%x == 1])
    return answer