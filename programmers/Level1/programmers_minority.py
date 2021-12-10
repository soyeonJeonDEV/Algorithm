#https://programmers.co.kr/learn/courses/30/lessons/12977
#소수 만들기

def solution(nums):
    temp = []
    cnt = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                temp.append(nums[i] + nums[j] + nums[k])
    
    for i in temp:
        flag = True
        for j in range(2,i):
            if i % j == 0:
                flag = False      
        if flag:
            cnt += 1
        
    return cnt