#두개 뽑아서 더하기
#https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    numbers.sort()
    
    for i in range(len(numbers)-1):
        for j in range(len(numbers)):
            sum = 0
            if i == j:
                pass
            else:
                sum = numbers[i] + numbers[j]
                if sum not in answer:
                    answer.append(sum)
    
    return sorted(answer)