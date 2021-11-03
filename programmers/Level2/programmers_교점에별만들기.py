#https://programmers.co.kr/learn/courses/30/lessons/87377?language=python3
#교점에 별 만들기
#런타임 에러
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
            
        x_min, y_min,x_max,y_max = d[0][0],d[0][1],d[0][0],d[0][1]
    for i in d:
        if x_min > i[0]:
            x_min = i[0]
        if x_max < i[0]:
            x_max = i[0]
        if y_min > i[1]:
            y_min = i[1]
        if y_max < i[1]:
            y_max = i[1]
    n = x_max - x_min
    m = y_max - y_min

    answer = [['.']*(n+1) for _ in range(m+1)]
    
    for x, y in d:
        answer[y_max - y][x - x_min] = '*'
    return [''.join(s) for s in answer]
    
  