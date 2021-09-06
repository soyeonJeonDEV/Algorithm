#문자열 내 p와 y의 개수
#https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
  return s.lower().count('p') == s.lower().count('y')

'''
def solution(s):
    p = 0
    y = 0
    answer = list(map(str, s))
    for i in range(len(answer)):
        if answer[i] == 'p'or answer[i] == 'P':
            p += 1
        elif answer[i] == 'y' or answer[i] == 'Y':
            y += 1
    if p == y:
        return True
    else:
        return False
'''