#짝지어 제거하기
#https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer = []
    for i in s:
        if len(answer) == 0:
            answer.append(i)
        else:
            #answer에 마지막으로 들어온 값과 i를 비교한 후 같으면 answer의 마지막 값을 빼고
            if answer[-1] == i:
                answer.pop()
            #그렇지 않으면 answer에 i값을 추가한다.
            else:
                answer.append(i)
    #answer가 존재하면 짝지어 제거하기 실패이므로 0 아니면 1을 리턴한다.            
    return 0 if answer else 1
