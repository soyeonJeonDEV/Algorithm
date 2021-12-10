#타겟넘버
#https://programmers.co.kr/learn/courses/30/lessons/43165
#답 보고 작성

def solution(numbers, target):
    tree = [0]
    for num in numbers:
        #sub_tree를 매번 초기화시킨다.
        sub_tree = []
        #1. 0 + 1, 0 - 1 의 값을 sub_tree에 집어넣고 tree에 대입한다.
        #2. tree = [1,-1]
        #3. 1 + 1, 1 - 1, -1 + 1, -1 - 1의 값을 sut_tree에 집어넣는다.
        #4. tree = [2,0,0,-2]
        #5. 반복
        for tree_num in tree:
            sub_tree.append(tree_num + num)
            sub_tree.append(tree_num - num)
        tree = sub_tree
    #tree의 값에 numbers로 더하고 빼는 모든 경우의 수가 들어갔다면 target값과 같은 개수를 반환한다. 
    return tree.count(target)
