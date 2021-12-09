#https://www.acmicpc.net/problem/9012
#괄호

n = int(input())
vps = [list(map(str,input())) for _ in range(n)]
for i in vps:
    answer = 'YES'
    stack = []
    for j in range(len(i)):
        if i[j] == '(':
            stack.append(i[j])

        else:
            if stack:
                stack.pop()
            else:
                answer = 'NO'
    if not stack:
        print(answer)
    else:
        answer = 'NO'
        print(answer)