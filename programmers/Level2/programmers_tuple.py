#튜플
#https://programmers.co.kr/learn/courses/30/lessons/64065
'''
import re
from collections import Counter
def solution(s):
    #정규식 {,}를 삭제하고 삭제한 자리에 뛰어쓰기를 한 후 tu에 저장
    tu = re.sub('[{,}]',' ', s)
    #int로 저장, 뛰어쓰기를 기준으로 list
    answer = list(map(int,tu.split()))
    #answer의 값들의 개수를 count
    cnt = Counter(answer)
    #count한 개수들의 빈도수대로 다시 정렬(2차원 배열)
    temp = cnt.most_common()
    result = []
    #2차원배열의 0번째 값만 result값에 저장
    for i in range(len(temp)):
        result.append(temp[i][0])
    return result
'''
#더 나은 풀이
import re
from collections import Counter

def solution(s):
    #'\d+'을 통해 0~9 또는 '+'를 모두 찾고, 그 값들의 개수를 count
    s = Counter(re.findall('\d+', s))
    # s.items()를 통해 배열로 만든 후 x[1]값 즉, count한 값을 큰수대로 나열한 배열에서 key값을 int로 변환하고 list함
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))