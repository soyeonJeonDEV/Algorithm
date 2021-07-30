#기능개발
#https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
  time = 0
  count = 0
  answer = []

  while len(progresses) > 0:
    if progresses[0] + time*speeds[0] >= 0:
      progresses.pop(0)
      speeds.pop(0)
      count += 1
    else:
      if count > 0:
        answer.append(count)
        count = 0
      time += 1
  answer.append(count)
  return answer