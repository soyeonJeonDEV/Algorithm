#실패율
#https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
#런타임에러
def solution(N, stages):
    answer = [i for i in range(1, N+1)]
    fault = {}
    score = []
    result = []

    for i in range(len(answer)):
        cnt = 0
        for j in range(len(stages)):
            if answer[i] == stages[j]:
                cnt += 1
        score.append(cnt)
        if i != 0:
            score[i] += score[i-1]

        if i == 0:
            fault[answer[i]] = cnt/len(stages)
        else:
            fault[answer[i]] = cnt/(len(stages)-score[i-1])
    
    result = sorted(fault, key=lambda k : fault[k], reverse = True)
    
    return result