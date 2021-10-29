#https://programmers.co.kr/learn/courses/30/lessons/67257
#수식최대화
from itertools import permutations

def calc(op, seq, exp):
    if exp.isdigit():
        return str(exp)
    else:
        if op[seq] == '*':
            split_data = exp.split('*')
            temp = []
            for s in split_data:
                temp.append(calc(op,seq+1,s))
            return str(eval('*'.join(temp)))
        
        if op[seq] == '+':
            split_data = exp.split('+')
            temp = []
            for s in split_data:
                temp.append(calc(op,seq+1, s))
            return str(eval('+'.join(temp)))
        
        if op[seq] == '-':
            split_data = exp.split('-')
            temp = []
            for s in split_data:
                temp.append(calc(op,seq+1,s))
            return str(eval('-'.join(temp)))
        
def solution(expression):
    answer = 0
    
    operations = list(permutations(['*','+','-'],3))
    
    for op in operations:
        result = abs(int(calc(op,0,expression)))
        
        if result > answer :
            answer = result
            
    return answer