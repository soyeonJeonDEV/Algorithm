def solution(numbers):
    answer = []
    for i in numbers:
        num1 = i
        num2 = i
        while True:
            num2 += 1
            a = bin(num1 ^ num2)
            bit = a.count('1')
            if 0<bit<=2:
                answer.append(num2)
                break
    return answer