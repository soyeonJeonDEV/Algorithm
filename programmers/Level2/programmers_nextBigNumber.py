#다음 큰 숫자
#https://programmers.co.kr/learn/courses/30/lessons/12911


def solution(n):
    i = 1
    while True:
        #조건1이 n 보다 큰 숫자이므로 n에다가 1을 더한다.
        result = n+i
        #2진수한 n에 1의 개수와 result의 1의 개수를 비교한 후 같으면 result를 반환한다.
        if bin(n)[2:].count("1") == bin(result)[2:].count("1"):
            return result
        #같지 않으면 i에 1을 더해서 result의 값을 1 키운다.
        else:
            i += 1