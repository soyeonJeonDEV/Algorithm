#https://www.acmicpc.net/problem/1780
# 종이의 개수

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

result = [0] * 3

def solution(x,y,n):
    num = graph[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if num != graph[i][j]:
                solution(x,y,n//3)
                solution(x,y+n//3,n//3)
                solution(x,y+n//3+n//3,n//3)
                solution(x+n//3,y,n//3)
                solution(x+n//3,y+n//3,n//3)
                solution(x+n//3,y+n//3+n//3,n//3)
                solution(x+n//3+n//3,y,n//3)
                solution(x+n//3+n//3,y+n//3,n//3)
                solution(x+n//3+n//3,y+n//3+n//3,n//3)
                return
    if num == -1:
        result.append(-1)
    elif num == 0:
        result.append(0)
    else:
        result.append(1)

solution(0,0,n)
print(result.count(-1))
print(result.count(0))
print(result.count(1))

# # 메모리 효율이 더 좋음(다른 사람 코드)
# def check(start_x : int, start_y : int, n : int):
#     temp = graph[start_x][start_y]
#     for i in range(n):
#         for j in range(n):
#             if temp != graph[start_x + i][start_y+j]:
#                 return False
#     return True


# def divide(start_x : int, start_y : int, n : int):
#     if check(start_x, start_y, n):
#         result[graph[start_x][start_y] + 1] += 1
#     else:
#         for i in range(3):
#             for j in range(3):
#                 divide(start_x + i*n//3, start_y + j*n//3, n//3)
#     return 

# divide(0,0,n)
# for i in result:
#     print(i)