#https://programmers.co.kr/learn/courses/30/lessons/12952
#N-Queen
#답보고 이해

def solution(n):
    cases = [0]
    def dfs(queens , next_queen):
        #컬럼체크
        if next_queen in queens:
            return
        #대각선체크
        for row, col in enumerate(queens):
            h = len(queens) - row
            if next_queen == col + h or next_queen == col -h:
                return 
            
        queens.append(next_queen)
        #끝체크
        if len(queens) == n:
            cases[0] += 1
            
        for next_queen in range(n):
            dfs(queens[:], next_queen) #deep copy of queens
            
            
    for next_queen in range(n):
        queens = []
        dfs(queens, next_queen)
        
    return cases[0]