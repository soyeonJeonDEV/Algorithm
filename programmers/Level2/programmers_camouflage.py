#위장
#https://programmers.co.kr/learn/courses/30/lessons/42578
#(한 옷의 종류수 + 1(안입는경우의수))* (한 옷의 종류수 + 1(안입는경우의수)) -(아무것도 안 입는경우의수)

def solution(clothes):
    count = 1
    cnt = {}
    
    for i in range(len(clothes)):
        cnt[clothes[i][1]] = 0
        
    for i in range(len(clothes)):
        cnt[clothes[i][1]] += 1
        
    if len(cnt) == 1:
        for i in cnt:
            return cnt[i]
    else:
        for i in cnt.values():
            count *= (i+1)
        count -= 1
    return count
'''
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
'''    