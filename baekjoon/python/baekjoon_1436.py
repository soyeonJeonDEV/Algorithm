#https://www.acmicpc.net/problem/1436
#영화감독 숌
#1666,2666...5666,6660,6661...

n = int(input())

name = 666
cnt = 0
while True:
    #name 안에 '666'이 들어가 있으면 카운팅
    if '666' in str(name):
        cnt += 1
        #카운팅한 값이랑 n이 같으면 name 출력
        if cnt == n: print(name) ; break
    #name안에 '666'이 생기기 전까지 1을 더한다.    
    name += 1