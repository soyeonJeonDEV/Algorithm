#3진법 뒤집기
#https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3
def solution(n):
    conversion = ''
    answer = 0
    
    while True:
        conversion = str(n%3) + conversion 
        n //= 3
        if n == 0:
            break
    for i in range(len(conversion)):
        answer += int(conversion[i])*3**i
        
    return answer
'''
    def solution(n):
      tmp = ''
      while n:
        tmp += str(n%3)
        n = n//3
      answer = int(tmp,3)
      return answer
'''