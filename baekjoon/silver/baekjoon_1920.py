#https://www.acmicpc.net/problem/1920
#수 찾기

"""
1. 아이디어
- n개의 숫자를 정렬
- m개를 for 돌면서, 이진탐색 
- 이진탐색 안에서 마지막 데이터 찾으면 1출력 아니면 0출력
2. 시간복잡도
- n개 입력값 정렬 = O(NlgN)
- m개를 n개중에서 탐색 = O(M*lgN)
- 총합 : O((M+N)lgN) > 가능
3. 자료구조
- n개 숫자 : int[]
- m개 숫자 : int[]
"""

n = int(input())
arr1 = list(map(int,input().split()))
arr1.sort() #이진탐색 가능
m = int(input())
arr2 = list(map(int,input().split()))

def search(st,ed,target):
    if st == ed:
        if arr1[st] == target:
            print(1)
        else:
            print(0)
        return

    mid = (st+ed)//2

    if arr1[mid] < target:
        search(mid+1,ed,target)
    else:
        search(st,mid,target)

for i in range(len(arr2)):
    search(0,n-1,arr2[i])

