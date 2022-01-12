#https://www.acmicpc.net/problem/3085
#사탕게임

def checkRow(a):
    maxNum = 1
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if a[i][j] == a[i][j-1]:
                cnt += 1
                maxNum = max(maxNum, cnt)
            else:
                cnt = 1
    return maxNum

def checkCol(a):
    maxNum = 1
    for j in range(n):
        cnt = 1
        for i in range(1,n):
            if a[i][j] == a[i-1][j]:
                cnt += 1
                maxNum = max(maxNum, cnt)
            else:
                cnt = 1
    return maxNum

n = int(input())
board = [list(map(str,input())) for _ in range(n)]

arr = board
result = 0

for i in range(n):
    for j in range(n-1):
        if arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1],arr[i][j]
            a = checkRow(arr)
            result = a if a > result else result
            a = checkCol(arr)
            result = a if a > result else result
            arr[i][j], arr[i][j+1] = arr[i][j+1],arr[i][j]

for i in range(n-1):
    for j in range(n):
        if arr[i][j] != arr[i+1][j]:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            a = checkRow(arr)
            result = a if a > result else result
            a = checkCol(arr)
            result = a if a > result else result
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
print(result)