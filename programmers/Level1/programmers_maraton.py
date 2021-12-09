#완주하지 못한 선수
#https://programmers.co.kr/learn/courses/30/lessons/42576
#답보고 작성

def solution(participant, completion):
  #참가자와 완주자를 정렬한다.
  participant.sort()
  completion.sort()
  #정렬을 했으므로 참가자와 완주자를 차례대로 비교한다.
  for p,c in zip(participant, completion):
    #참가자 이름과 완주자 이름이 같지 않으면 참가자는 완주를 하지 못한 것이므로 참가자의 이름을 반환한다.
    if p != c :
      return p
  #마지막까지 참가자 이름과 완주자 이름이 같으면 마지막 참가자의 이름만 반환한다.
  return participant.pop()
