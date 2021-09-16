def solution(msg):
    msg = list(msg)
    alpha = [chr(x) for x in range(ord('A'),ord("Z")+1)]
    index = {}
    answer = [msg[0]]
    temp = msg[0]
    t = ''
    
    for i in range(len(alpha)):
        index[alpha[i]] = i+1

    for i in range(len(msg)-1):
        temp += msg[i+1]
        t = msg[i+1]
        if temp not in index:
            index[temp] = len(index) + 1
            temp = msg[i+1]
            answer.append(t)
        else:
            answer.pop()           
            answer.append(temp)
    return [index.get(i) for i in answer]