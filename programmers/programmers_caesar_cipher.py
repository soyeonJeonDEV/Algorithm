#시저암호
#https://programmers.co.kr/learn/courses/30/lessons/12926

#내가 푼 풀이
def solution(s, n):
    s = list(s)
    answer = 0
    result = ''
    for i in s:
        if i.isupper():
            if ord(i) + n > ord('Z'):
                answer = ord(i) + n - ord('Z') + ord('A') - 1
            else:
                answer = ord(i)+n
        elif i.islower():
            if ord(i) + n > ord('z'): 
                answer = ord(i) + n - ord('z') + ord('a') - 1
            else:
                answer = ord(i)+n
        else:
            answer = 32
        result += chr(answer)
    return result
'''
#간단한 풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
'''