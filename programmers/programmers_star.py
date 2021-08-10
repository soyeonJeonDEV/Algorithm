#직사각형 별찍기
#https://programmers.co.kr/learn/courses/30/lessons/12969

'''
#내가 푼 풀이
a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*' * a)
'''
#신박한 풀이
a, b = map(int, input().strip().split(' '))
answer = (a*'*' + '\n')*b
print(answer)