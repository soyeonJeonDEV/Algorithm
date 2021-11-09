def solution(numbers):
    answer = []
    for i in numbers:
        num1_bin = str(bin(i))[2:]
        num2 = i
        while True:
            num2 += 1
            num2_bin = str(bin(num2))[2:]
            bit = 0
            z = len(num1_bin)+2
            num1_bin = num1_bin.rjust(z,'0')
            num2_bin = num2_bin.rjust(z,'0')            
            for j in range(len(num1_bin)):
                if num1_bin[j] != num2_bin[j]:
                    bit += 1
            if 0 < bit <= 2:
                answer.append(num2)
                break
                
    return answer