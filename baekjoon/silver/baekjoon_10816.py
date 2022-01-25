# 숫자 카드 2
from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

arr.sort()


#Counter 함수를 사용한 결과

# C = Counter(arr)
# for i in arr2:
#     if i in arr:
#         print(C.get(i),end =" ")
#     else:
#         print(0, end=" ")


# 이분탐색을 사용한 결과

# def search(st,ed,num):

#     if st > ed:
#         return 0

#     mid = (st+ed)//2

#     if num == arr[mid]:
#         return  arr[st:ed+1].count(num)
#     elif arr[mid] > num:
#          return search(st,mid-1,num)
#     else:
#          return search(mid+1,ed, num)
    

# for num in arr2:
#     a = search(0,n-1,num)
#     print(a,end=" ")


temp  = 0

