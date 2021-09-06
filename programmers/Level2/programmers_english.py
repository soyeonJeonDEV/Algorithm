#영어 끝말잇기
#https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    for i in range(len(words)-1):
        #첫번째 단어의 끝과 두번째 단어의 처음이 같거나 words를 i까지 나타낸 배열에서 word[i+1] 단어가 포함되어 있다면 
        if words[i+1] in words[:i] or words[i][-1] != words[i+1][0]:
            #탈락하는 사람의 번호 : 나머지+1, 몇번째 차례에 탈락하는 지 : 몫+1
            return [(i+1)%n+1, (i+1)//n+1]
    #전부 통과했으면 [0,0]을 return 
    return [0,0]