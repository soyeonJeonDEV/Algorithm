#베스트앨범
#https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    g = {}
    p = [i for i in enumerate(plays)]
    answer = []
    for i in range(len(genres)):
        if genres[i] in g:
            g[genres[i]] += plays[i]
        else:
            g[genres[i]] = plays[i]
    g = sorted(g.items(),key=lambda x:-x[1])
    for i in range(len(g)):
        temp = []
        for j in range(len(genres)):
            if g[i][0] == genres[j]:
                temp.append(p[j])
        temp = sorted(temp,key=lambda x:-x[1])
        for i in temp[:2]:
            answer.append(i[0])
    return answer