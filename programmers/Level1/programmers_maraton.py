#완주하지 못한 선수
#https://programmers.co.kr/learn/courses/30/lessons/42576
#답보고 공부 후 다시 작성

#1
def solution(participant, completion):
  participant.sort()
  completion.sort()
  for p,c in zip(participant, completion):
    if p != c :
      return p
    return participant.pop()
#2
    '''
    import collections
    def solution(participant, completion):
      answer = collections.Counter(participant) - collections.Counter(completion)
      return list(answer.key())[0]
      '''