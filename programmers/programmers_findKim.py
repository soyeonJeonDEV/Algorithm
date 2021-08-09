#서울에서 김서방 찾기
#https://programmers.co.kr/learn/courses/30/lessons/12919
#내가 푼 풀이
def solution(seoul):
    for x in range(len(seoul)):
        if seoul[x] == "Kim":
            return "김서방은 "+str(x)+"에 있다"
'''
#다른 풀이
def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index("Kim"))
'''