#https://www.acmicpc.net/problem/2231
#분해합

n = int(input())

for i in range(n+1):
    answer = i
    s = str(i)
    for j in range(len(s)):
        answer += int(s[j])
    if answer == n:
        print(int(s))
        break
        
else:
    print(0)