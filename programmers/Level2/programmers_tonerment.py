#예상 대진표
#https://programmers.co.kr/learn/courses/30/lessons/12985
'''
def solution(n,a,b):
    #temp에 1~n 까지 수를 넣은 배열 생성
    temp = [x for x in range(1,n+1)]
    #첫 경기부터 만날 수 있기 때문에 cnt의 값은 1
    cnt = 1
    # a와 b가 만날때까지 반복
    while True:
        # 초기화
        answer = []
        # 둘씩 비교해야하기 때문에 
        for i in range(0,len(temp),2):
            # a와 b가 만났을 때
            if temp[i] == a and temp[i+1] == b or temp[i] == b and temp[i+1] == a:
                return cnt
            # a랑 b가 만나지 않았을 때 a를 answer에 삽입
            if temp[i] == a or temp[i+1] == a:
                answer.append(a)
            # a랑 b가 만나지 않을 때 b를 answer에 삽입
            elif temp[i] == b or temp[i+1] == b:
                answer.append(b)
            # a,b 둘다 없을 때는 아무 숫자나 answer에 삽입 
            else:
                answer.append(temp[i])
        #1라운드 끝날때 마다 cnt에 1을 더한다.
        cnt += 1
        #temp에 answer을 대입
        temp = answer
    return answer
'''
def solution(n,a,b):
    answer = 0
    #두 참가자의 번호가 같아지는 라운드 확인
    while a != b:
        answer += 1
        #각 번호는 다음 라운드에서 (n+1)//2의 번호를 부여
        a = (a+1)//2
        b = (b+1)//2
    return answer    