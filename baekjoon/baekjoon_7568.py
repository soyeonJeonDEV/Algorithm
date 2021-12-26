#https://www.acmicpc.net/problem/7568
#덩치

n = int(input())
arr  = [list(map(int, input().split())) for _ in range(n)]
answer = []
for i in range(len(arr)):
    cnt = 1
    for j in range(len(arr)):
        if i != j:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                cnt += 1
    answer.append(cnt)

for i in range(len(answer)):
    print(answer[i],end =" ")
