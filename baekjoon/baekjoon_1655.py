#https://www.acmicpc.net/problem/1655
#가운데를 말해요
#heapq 모듈을 사용

import sys
import heapq
input = sys.stdin.readline

n = int(input())
left, right = [],[]

for _ in range(n):
    num = int(input())
    if len(left) == len(right):
        #최댓값 정렬
        heapq.heappush(left,(-num,num))
    else:
        #최소값 정렬
        heapq.heappush(right,(num,num))

    if right and left[0][1] > right[0][1]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        print(left_value)
        print(right_value)
        heapq.heappush(right,(left_value,left_value))
        heapq.heappush(left,(-right_value,right_value))
    print(left[0][1])