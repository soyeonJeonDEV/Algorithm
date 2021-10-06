#스도쿠
#https://www.acmicpc.net/problem/2580

sudo = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i,j) for i in range(9) for j in range(9) if sudo[i][j] == 0]

def is_promising(i,j):
    promising = [1,2,3,4,5,6,7,8,9]

    for k in range(9):
        if sudo[i][k] in promising:
            promising.remove(sudo[i][k])
        if sudo[k][j] in promising:
            promising.remove(sudo[k][j])
    i //= 3
    j //= 3

    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudo[p][q] in promising:
                promising.remove(sudo[p][q])

    return promising

flag = False

def dfs(x):
    global falg
    
            
