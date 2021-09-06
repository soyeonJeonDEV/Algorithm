#뉴스 클러스터링
#https://programmers.co.kr/learn/courses/30/lessons/17677
'''
#floor를 쓰기 위해 
import math
def solution(str1, str2):
    #두문자씩 끊어서 저장하고, 알파벳만 있는거, 글자수가 2개인것만 저장하고, 대문자로 변환
    a = [str1[x:x+2].upper() for x in range(len(str1)) if str1[x:x+2].isalpha() and len(str1[x:x+2]) == 2]
    b = [str2[x:x+2].upper() for x in range(len(str2)) if str2[x:x+2].isalpha() and len(str2[x:x+2]) == 2] 
    #합집합은 전체수 - 교집합
    sum1 = len(a+b)
    multi = 0
    #다중집합이므로 b안에 a가 들어가 있는걸 제거하고 개수를 더한다.
    for i in a:
        if i in b:
            multi += 1
            b.remove(i)
    sum1 -= multi
    # 합, 교집합이 0일때는 65536을 return하고 아니면 자카드 유사도를 구하고 65536을 곱한 후 소수점을 버린다.
    return 65536 if sum1 == 0 and multi == 0 else math.floor((multi/sum1)*65536)

  '''
  # 더 좋은 풀이
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)