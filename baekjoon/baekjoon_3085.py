#https://www.acmicpc.net/problem/3085
#사탕게임

import copy
import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(str,input())) for _ in range(n)]

def check(arr):
    cnt = 0
    for i in range(len(arr)):
        cntRow = 1
        cntCol = 1
        for j in range(len(arr)-1):
            if arr[i][j] == arr[i][j+1]:
                cntRow += 1
            if arr[j][i] == arr[j+1][i]:
                cntCol += 1
        cnt = max(cnt, cntRow, cntCol)
        if cnt == len(board):
            break
    return cnt


answer = check(board)

#행과 열의 사탕을 swap한 값
for i in range(len(board)):
    for j in range(len(board)-1):
        row = copy.deepcopy(board)
        column = copy.deepcopy(board)
        if board[i][j] != board[i][j+1]:
            row[i][j], row[i][j+1] = board[i][j+1], board[i][j]
            a = check(row)
            answer = max(a, answer)
        if board[j][i] != board[j+1][i]:
            column[j][i], column[j+1][i] = board[j+1][i], board[j][i]
            a = check(column)
            answer = max(a,answer)
print(answer)
