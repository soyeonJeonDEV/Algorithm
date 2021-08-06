#정수 내림차순으로 배치하기
#https://programmers.co.kr/learn/courses/30/lessons/12933
'''
#내가 푼 풀이
def solution(n):
    n = str(n)
    answer = sorted(list(n), reverse = True)
    result =''
    for i in range(len(answer)):
        result += answer[i]
        
    return int(result)
'''
#간단한 풀이
def solution(n):
    return int("".join(sorted(str(n),reverse=True)))