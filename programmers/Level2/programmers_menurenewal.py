#메뉴리뉴얼
#https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter
def solution(orders, course):

    answer = []
    for x in range(len(course)):
        cnt = ''
        menu = []
        for i in orders:
            temp = sorted(list(i))
            temp = list(combinations(temp,course[x]))
            for j in range(len(temp)):
                t = "".join(temp[j])
                menu.append(t)        
        cnt=Counter(menu)
        for k, v in cnt.items():
            if max(cnt.values()) == v and max(cnt.values()) >= 2:
                answer.append(k)
    return sorted(answer)