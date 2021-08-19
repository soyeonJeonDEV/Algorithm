#JadenCase 문자열 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    #s를 전부 소문자로 변환 후 list에 담는다.
    s = list(s.lower())
    #첫문자는 무조건 대문자로 
    s[0] = s[0].upper()
    #s[i]가 공백이라면 다음 문자는 무조건 대문자가 되도록 한다.
    for i in range(len(s)-1):
        if s[i] == ' ':
            s[i+1] = s[i+1].upper()
    return "".join(s)