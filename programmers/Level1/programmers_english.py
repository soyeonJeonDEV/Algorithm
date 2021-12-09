#숫자 문자열과 영단어
#https://programmers.co.kr/learn/courses/30/lessons/81301


def solution(s):
    alpha = {'one':'1', 'two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}

    for i,j in alpha.items():
        s = s.replace(i,j)
            
    return int(s)