#k번째 수 
#https://programmers.co.kr/learn/courses/30/lessons/42748
#답보고 공부 후 다시 작성
#더 좋은 풀이
'''
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command[0],command[1],command[2]
        slice = array[i-1:j]
        slice.sort()
        answer.append(slice[k-1])

    return answer
'''
def solution(array,commands):
  return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1],commands))