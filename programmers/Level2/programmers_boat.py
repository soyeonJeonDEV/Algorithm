#구명보트
#https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people.sort()
    cnt = 0
    i = 0
    j = len(people)-1
    while i <= j:
        cnt += 1
        if people[j] + people[i] <= limit:
            i += 1
        j -= 1
    return cnt