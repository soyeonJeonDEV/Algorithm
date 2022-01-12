#https://www.acmicpc.net/problem/2309
#일곱난쟁이

arr = [int(input()) for _ in range(9)]
arr.sort()
for i in range(len(arr)):
    for j in range(len(arr)):
        if i != j and sum(arr) - arr[i] - arr[j] == 100:
                a = arr[i]
                b = arr[j]
                break

arr.remove(a)
arr.remove(b)

for i in arr:
    print(i)
