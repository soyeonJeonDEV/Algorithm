#오픈채팅방
#https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    temp = {}
    
    for i in record:
        row = i.split()
        if row[0] == "Enter" or row[0] == "Change":
            temp[row[1]] = row[2]
    for i in record:
        row = i.split()
        if row[0] == "Enter":
            answer.append(temp[row[1]] + "님이 들어왔습니다.")
        elif row[0] == "Leave":
            answer.append(temp[row[1]] + "님이 나갔습니다.")

    return answer