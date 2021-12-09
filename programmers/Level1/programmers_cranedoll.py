#크레인인형뽑기
#https://programmers.co.kr/learn/courses/30/lessons/64061

# def solution(board, moves):
#     answer = []
#     cnt = 0
#     n = len(board)
    
#     for i in moves:
#         for j in range(n):
#             if board[j][i-1] == 0:
#                 continue
#             else:
#                 if len(answer) == 0:
#                     answer.append(board[j][i-1])
#                     board[j][i-1] = 0
#                     break
#                 else:
#                     if answer[-1] == board[j][i-1]:
#                         answer.pop()
#                         cnt += 1
#                         board[j][i-1] = 0
#                         break
#                     else:
#                         answer.append(board[j][i-1])
#                         board[j][i-1] = 0
#                         break
            
#     return cnt*2

# 더 간단한 풀이
def solution(board, moves):
    basket = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                 pass
            else:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                break

        if len(basket) >= 2 and basket[len(basket)-1] == basket[len(basket)-2]:
            basket.pop(-1)
            basket.pop(-1)
            answer += 1
    return answer * 2

