#https://programmers.co.kr/learn/courses/30/lessons/12977
#소수 만들기

def solution(nums):
    answer = 0
    nums.sort()
    temp = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                temp.append(nums[i]+nums[j]+nums[k])
    
    flag = True
    for i in temp:
        for j in range(2,i):
            if i%j == 0:
                flag = False
                break
        if flag:
            answer += 1
        flag = True
    return answer