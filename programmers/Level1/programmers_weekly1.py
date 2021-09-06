#위클리챌린지1주차
#부족한금액 계산하기
#https://programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    answer = 0
    total = 0
    
    for i in range(count):
        total += price*(i+1)
        print(total)

    if total - money <= 0:
        return 0
    else:
        return total - money 

