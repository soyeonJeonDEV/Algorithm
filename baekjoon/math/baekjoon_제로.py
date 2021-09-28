n = int(input())
answer = []
for i in range(n):
    a = int(input())
    answer.append(a)
    if a == 0:
        answer.pop()
        answer.pop()
print(sum(answer))