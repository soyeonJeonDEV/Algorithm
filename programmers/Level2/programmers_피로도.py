#https://programmers.co.kr/learn/courses/30/lessons/87946?language=python3
#피로도
#weekly
from itertools import permutations

def solution(k, dungeons):
    a = list(permutations([i for i in dungeons], len(dungeons)))
    answer = []
    for i in a:
        cnt = 0
        tt = k 
        for j in range(len(i)):
            if i[j][0] <= tt:
                tt -= i[j][1]
                cnt += 1
        answer.append(cnt)
        
    return max(answer)