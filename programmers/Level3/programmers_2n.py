#https://programmers.co.kr/learn/courses/30/lessons/12900
#2*n 타일링

#내가 푼 풀이
'''
def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2])%1000000007
    
    return dp[n]
    
'''
# 효율성 더 좋은 풀이

def solution(n):
    a,b = 1,1
    
    for i in range(1, n):
        a,b = b, (a+b)%1000000007
        
    return b