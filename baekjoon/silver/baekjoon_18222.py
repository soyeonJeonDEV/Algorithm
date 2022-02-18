# 투에-모스 문자열
# 메모리 초과
# 분할 정복으로 풀기

import sys

input = sys.stdin.readline

k = int(input())

def bfs(n):
    #x는 맨 처음에 "0"으로 시작한다.
    x = '0'

    while True:

        xx = list(x)

        if len(x) >= n+1:
            return x[n-1]
        #2. x에서 0을 1로, 1을 0으로 뒤바꾼 문자열 x' 를 만든다.
        for i in range(len(xx)):
            if xx[i] == '0':
                xx[i] = '1'
            else:
                xx[i] = '0'
        #  3. x의 뒤에 xx 를 붙인 문자열을 x로 다시 정의한다.
        xx = "".join(xx)
        x = x+ xx




answer = bfs(k)
print(answer)
