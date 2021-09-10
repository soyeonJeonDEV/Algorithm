#문자열압출
#https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    hub = {0:len(s)}
    
    for i in range(1,len(s) + 1):
        start = 0 
        stack = 0
        word = ""
        # 압축할 패턴
        pattern = s[0:i]
        print("---")
        while True:
            #s의 길이보다 start가 커지면
            if start > len(s):
                #i씩 나눠서 남는 s 문자열을 더한다.
                word += s[start-i:]
                hub[i] = len(word)
                break
            #앞 패턴이랑 자른 문자열이 같으면 stack을 쌓는다
            if pattern == s[start:start+i]:
                stack += 1
            #패턴이 같지 않다면 stack이 쌓인만큼 숫자를 앞에두고 압축
            else:
                word += (str(stack) if stack > 1 else "") + str(pattern)
                #스택 초기화
                stack = 1
                #압축한 문자열 다음 문자를 패턴으로 둔다
                pattern = s[start:start+i]
                if min(hub.values()) < len(word):
                    break
            #start에 1씩 더한다
            start += i
    answer = min(hub.values())
    print(hub)
    return answer