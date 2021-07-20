#숫자 문자열과 영단어
#https://programmers.co.kr/learn/courses/30/lessons/81301
#답 보고 공부 후 다시 작성
#더 좋은 풀이
'''
keys = ('zero','one','two','three','four','five','six','seven','eight','nine')
values = (str(i) for i in range(10))
number_dict = dict(zip(keys,values))

def solution(s):

    word = ''
    result =''

    for ch in s:
        if ch.isdigit():
            result += ch
        else:
            word += ch
            if word in keys:
              result += number_dict[word]
              word = ''
    return int(result)
'''
number_dict = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

def solution(s):
  answer = s
  for key, value in number_dict.items():
    answer = answer.replace(key,value)
  return int(answer)
