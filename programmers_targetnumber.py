#타겟넘버
#https://programmers.co.kr/learn/courses/30/lessons/43165
#공부 후 다시 작성
def solution(numbers, target):
  tree = [0]
  for num in numbers:
    sub_tree = []
    for tree_num in  tree:
      sub_tree.append(tree_num + num)
      sub_tree.append(tree_num - num)
    tree = sub_tree
  return tree.count(target)
  '''
  def solution(numbers, target):
    if not numbers and target == 0:
      return 1
    elif not numbers:
      return 0
    else :
      return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
  '''
  '''
  from itertools import product
  def solution(numbers, target):
    l = [(x,-x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
  '''
