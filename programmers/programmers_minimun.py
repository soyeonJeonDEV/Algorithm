#최솟값 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12941
#작은 수와 큰수를 곱해서 더하면 최소값
def solution(A,B):
    answer = 0
    A.sort(reverse=False)
    B.sort(reverse=True)
    
    for i,j in zip(A,B):
        answer += i*j

    return answer