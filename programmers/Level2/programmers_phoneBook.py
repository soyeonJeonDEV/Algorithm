#전화번호 목록
#https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    #phone_book을 정렬해서 앞뒤 문자열 비교만 해도 되도록
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        sl = len(phone_book[i])
        #정렬했을때 글자수가 더 작은 문자가 앞에 오니 다음 인자를 앞 인자의 글자수만큼 자르고 같은지 비교
        if phone_book[i] == phone_book[i+1][:sl]:
            return False
    return True