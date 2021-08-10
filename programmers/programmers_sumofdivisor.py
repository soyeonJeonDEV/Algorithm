#약수의 합
#https://programmers.co.kr/learn/courses/30/lessons/12928

#내가 푼 풀이
def solution(n):
    answer = [ i+1 for i in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if answer[i]*answer[j] == n:
                result.append(answer[i])
                result.append(answer[j])
            
    return sum(list(set(result)))

'''
#간단한 풀이
def solution(n):
    #n/2의 수 들만 검사하면 시간단축
    return n + sum([i for i in range(1, n//2 + 1) if n % i == 0])
'''