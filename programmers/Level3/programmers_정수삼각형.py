#https://programmers.co.kr/learn/courses/30/lessons/43105
#정수삼각형

def solution(triangle):
    n = len(triangle)
    
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            elif j == i:
                triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
            else:
                triangle[i][j] = max(triangle[i-1][j],triangle[i-1][j-1]) + triangle[i][j]
    return max(triangle[-1])