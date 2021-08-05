#핸드폰 번호 가리기
#https://programmers.co.kr/learn/courses/30/lessons/12948
'''
#내가 푼 풀이
def solution(phone_number):
    num = list(phone_number)
    answer = ''
    for i in range(len(num)-4):
        num[i] = '*'
    for i in range(len(num)):
        answer += num[i]
    
    return answer
'''
#더 좋은 풀이
def solution(phone_number):
  # '*'를 번호개수에서 4개를 빼서 곱한 후 phone_number 뒤에 4자리를 더한다.
  return '*' * (len(phone_number)-4) + phone_number[-4:]