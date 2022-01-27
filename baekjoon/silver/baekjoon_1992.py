#https://www.acmicpc.net/problem/1992
# 쿼드트리

n = int(input())
graph = [list(map(int,input())) for _ in range(n)]

result = []

def solution(x,y,n):
    color = graph[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != color:
                result.append('(')
                solution(x,y,n//2)
                solution(x,y+n//2, n//2)
                solution(x+n//2,y,n//2)
                solution(x+n//2,y+n//2,n//2)
                result.append(')')
                return

    if color == 0:
        result.append('0')
    else:
        result.append('1')

solution(0,0,n)

print("".join(result))