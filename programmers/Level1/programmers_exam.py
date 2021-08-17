#모의고사
#https://programmers.co.kr/learn/courses/30/lessons/42840

'''
#내가 푼 풀이
def solution(answers):
    a = [1,2,3,4,5]*2000
    b = [2,1,2,3,2,4,2,5]*1250
    c = [3,3,1,1,2,2,4,4,5,5]*1000
    ac = 0
    bc = 0
    cc = 0
    result = []
    maxv = []
    
    for i in range(len(answers)):
        if a[i] == answers[i]:
            ac += 1
        if b[i] == answers[i]:
            bc += 1
        if c[i] == answers[i]:
            cc += 1
    result.append(ac)
    result.append(bc)
    result.append(cc)
    for i in range(len(result)):
        if max(result) == result[i]:
            maxv.append(i+1)
        
    return maxv

    '''

    #더 좋은 풀이
def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    result = []
    
    for idx, answer in enumerate(answers):
        if answer == a[idx%len(a)]:
            score[0] += 1
        if answer == b[idx%len(b)]:
            score[1] += 1
        if answer == c[idx%len(c)]:
            score[2] += 1
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    return result