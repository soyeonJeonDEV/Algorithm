'''
def solution(skill, skill_trees):
    skill = list(skill)
    cnt = 0
    for i in skill_trees:
        temp = i
        answer = []
        l = 0
        for j in range(len(temp)):
            if temp[j] in skill :
                answer.append(temp[j])
        for j in range(len(answer)):
            if answer[j] == skill[j]:
                l += 1
        if l == len(answer):
            cnt += 1
    return cnt
'''
def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        skill_list = ''
        for sk in skills:
            if sk in skill:
                skill_list += sk
        if skill_list == skill[0:len(skill_list)]:
            answer += 1
    return answer