#https://www.acmicpc.net/problem/2559
#수열
"""
1. 아이디어
- 투포인터를 활용
- for문으로, 처음에 k개값을 저장
- 이때마다 최대값을 갱신
2. 시간복잡도
- O(n) = le5 > 가능
3. 자료구조
- 각 수자를 n개 저장 배열 : int[]
    - 숫자들 최대 100 > int 가능
- k개의 값을 저장 변수 : int
    - 최대 : k*100 = 1e5 *100 = 1e7 > int 가능
- 최대값 : int
"""
import sys

input = sys.stdin.readline

n,k = map(int,input().split())
day = list(map(int,input().split()))
each = 0

#k개를 더해주기
for i in range(k):
    each += day[i]
maxv = each

#다음 인덱스 더해주고, 이전 인덱스 빼주기
for i in range(k,n):
    each += day[i]
    each -= day[i-k]
    maxv = max(maxv, each)
print(maxv)

#시간초과(O(nk)는 2억이상이기때문에)
# for i in range(len(day)-k):
#     s = 0
#     for j in range(k):
#         s += day[i+j]  
#     maxx = max(s, maxx)

# print(maxx)



