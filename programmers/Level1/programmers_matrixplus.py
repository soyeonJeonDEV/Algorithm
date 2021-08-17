#행렬의 덧셈
#https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = []
    tmp = []
    for i,j in zip(arr1,arr2):
        for x,z in zip(i,j):
            tmp.append(x+z)
            print(tmp)
        answer.append(tmp)
        tmp = []
    return answer