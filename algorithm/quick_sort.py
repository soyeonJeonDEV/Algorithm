# 대표적인 분할 정복 알고리즘
# 내부 정렬 : 추가 리스트를 사용하지 않음
# divide : 기준 원소(pivot) 를 정해서 좌우 분할
# conquer : 왼쪽과 오른쪽 리스트를 각각 재귀적으로 퀵정렬
# obtain : 정렬된 리스트 리턴

# 기준 원소(pivot)은 어떻게 정하나?
# 편의상 리스트의 첫 원소를 기준원소로 정하자

# 기준원소로 어떻게 나눌 수 있는가?
# 두 개의 인덱스 (i,j)로 비교, 교환

def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array)//2]
    less, more, equal = [],[],[]
    
    for each in range(len(array)):
        each = array.pop()
        if each < pivot:
            less.append(each)
        elif each > pivot:
            more.append(each)
        else:
            equal.append(each)

    return quicksort(less) + equal + quicksort(more)

S = [15,22,13,27,12,10,20,25]
print('before : ', S)
print('after : ', quicksort(S))

