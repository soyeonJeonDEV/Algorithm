#k번째 수 
#https://programmers.co.kr/learn/courses/30/lessons/42748

# def solution(array, commands):
#     answer = []
#     for i in commands:
#         ar = sorted(array[i[0]-1:i[1]])
#         answer.append(ar[i[2]-1])
        
#     return answer

#더 간단한 풀이
def solution(array,commands):
  return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1],commands))