#같은 숫자는 싫어
#https://programmers.co.kr/learn/courses/30/lessons/12906
'''
#내가 푼 풀이
def solution(arr):
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            arr[i] = "*"
    return [x for x in arr if x != '*']
'''
# answer에 들어온 마지막 문자와 answer에 들어올 문자와 비교한 후 같으면 통과하고, 다르면 추가하는 알고리즘
def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    return answer