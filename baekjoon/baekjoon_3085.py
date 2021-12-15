#https://www.acmicpc.net/problem/3085
#사탕게임

import copy
import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(str,input())) for _ in range(n)]

def checkRow(arr, line):
    cntRow = 1
    for i in range(len(arr)-1):
        if arr[line][i] == arr[line][i+1]:
            cntRow += 1
    return cntRow

def checkCol(arr, line):
    cntCol = 1
    for i in range(len(arr)-1):
        if arr[i][line] == arr[i+1][line]:
            cntCol += 1
    return cntCol

answer = 0
a = 0
b = 0

for i in range(len(board)):
    answer = max(checkRow(board,i), checkCol(board,i), answer)

#행과 열의 사탕을 swap한 값
for i in range(len(board)):
    for j in range(len(board)-1):
        row = copy.deepcopy(board)
        column = copy.deepcopy(board)
        if board[i][j] != board[i][j+1]:
            row[i][j], row[i][j+1] = board[i][j+1], board[i][j]
            a = checkRow(row,i)
            b = checkCol(row,j)
            answer = max(a,b,answer)
        if board[j][i] != board[j+1][i]:
            column[j][i], column[j+1][i] = board[j+1][i], board[j][i]
            a = checkRow(column,i)
            b = checkCol(column,j)
            answer = max(a,b,answer)

print(answer)
