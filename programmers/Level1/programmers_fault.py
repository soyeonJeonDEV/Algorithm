#실패율
#https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    n = len(stages)
    stages = sorted(stages)
    answer = {}
    
    for i in range(1,N+1):
        cnt = 0
        for j in stages:
            if i == j:
                cnt += 1
        if cnt == 0:
            answer[i] = 0
        else:
            answer[i] = cnt/n
            n -= cnt
    answer = sorted(answer.items(), key=lambda x:x[1],reverse=True )
    return [i[0] for i in answer]