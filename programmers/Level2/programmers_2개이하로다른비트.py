def solution(numbers):
    answer = []
    for i in numbers:
        bin_num = list('0' + bin(i)[2:])
        #rfind : 오른쪽부터 처음 등장하는 위치를 찾음
        #짝수의 경우 2진수 마지막 숫자는 '0'
        idx = ''.join(bin_num).rfind('0')
        bin_num[idx] = '1'
        if i % 2 == 1:
            bin_num[idx+1] = '0'
        answer.append(int(''.join(bin_num),2))
    return answer