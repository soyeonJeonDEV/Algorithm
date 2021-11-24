#https://www.acmicpc.net/problem/1316
#그룹 단어 체커

n = int(input())
cnt = 0
for i in range(n):
    word = input()
    flag = True
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
           if word[j] in word[j+1:]:
               flag = False
    if flag == True:
        cnt += 1

        

print(cnt)

