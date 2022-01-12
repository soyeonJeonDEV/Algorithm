#https://www.acmicpc.net/problem/10773
#제로
n = int(input())
answer = []
for i in range(n):
    a = int(input())
    answer.append(a)
    if a == 0:
        answer.pop()
        answer.pop()
print(sum(answer))