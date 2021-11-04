#https://programmers.co.kr/learn/courses/30/lessons/87377?language=python3
#교점에 별 만들기
#런타임 에러(x,y의 최소값 최대값이 틀려 인덱스값 오류로 인해 런타임 에러 발생) -> 수정 
from itertools import combinations
def solution(line):
    d = []
    dd = list(combinations(line, 2))

    for i in dd:
        if (i[0][0]*i[1][1] - i[0][1]*i[1][0]) != 0:
            x = (i[0][1]*i[1][2] - i[0][2]*i[1][1])/(i[0][0]*i[1][1] - i[0][1]*i[1][0])
            y = (i[0][2]*i[1][0] - i[0][0]*i[1][2])/(i[0][0]*i[1][1] - i[0][1]*i[1][0])

        if abs(x % 1) == 0 and abs(y % 1) == 0 and [x,y] not in d:
            d.append([int(x),int(y)])
    x_list = []
    y_list = []
    for i in d:
        x_list.append(i[0])
        y_list.append(i[1])
    n = max(x_list) - min(x_list)
    m = max(y_list) - min(y_list)
    
    answer = [['.']*(n+1) for _ in range(m+1)]
    
    for x,y in d:
        answer[max(y_list)-y][x-min(x_list)] = '*'
        
    return ["".join(s) for s in answer]