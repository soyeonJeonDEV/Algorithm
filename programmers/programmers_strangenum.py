#이상한 숫자만들기
#https://programmers.co.kr/learn/courses/30/lessons/12930
#내가 푼 문제
def solution(s):
    s = list(map(str, s.split(" ")))
    answer = ''
    for i in s:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    return answer[:-1]
