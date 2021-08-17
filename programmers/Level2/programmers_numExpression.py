#숫자의 표현
#https://programmers.co.kr/learn/courses/30/lessons/12924
def solution(n):
    cnt = 0
    #1부터 n까지의 숫자
    for i in range(1, n+1):
        sum = 0
        num = i
        #'1+2+...','2+3+...'로 sum을 구해서 n 값이 되면 cnt값을 1씩 올린다.
        for num in range(num,n+1):
            sum += num
            if sum == n:
                cnt += 1
                break
            # 효율성을 올리기 위해 sum이 n보다 크면 for문을 나간다.
            elif sum > n:
                break
    return cnt