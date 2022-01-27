# https://www.acmicpc.net/problem/2630
# 색종이 만들기

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

# 첫 색상이 나머지 색상과 같은지 확인 후 틀린 것이 있으면,
# 틀린 구역을 다시 네 구역으로 나누어 다시 색상이 같은 것을 확인

result = []

def solution(x,y,n):
    color = graph[x][y]
    for i in range(x, x+n): 
        for j in range(y, y+n):
            if  graph[i][j] != color:
                solution(x,y,n//2) # 1사분면
                solution(x,y+n//2, n//2) # 2사분면
                solution(x+n//2, y, n//2) # 3사분면
                solution(x+n//2, y+n//2,n//2) # 4사분면
                return 
    if color == 0:
        result.append(0)
    else:
        result.append(1)


solution(0,0,n)
print(result.count(0))
print(result.count(1))