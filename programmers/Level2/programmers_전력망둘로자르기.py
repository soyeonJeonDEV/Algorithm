#https://programmers.co.kr/learn/courses/30/lessons/86971
#전력망을 둘로 나누기
def solution(n, wires):
    trees = {k:set() for k in range(1,n+1)}
    answer = n
    
    for i,j in wires:
        trees[i].add(j)
        trees[j].add(i)
    for i,j in wires:
        trees[i].remove(j)
        trees[j].remove(i)
        result = abs(2*dfs(i, trees) - n)
        trees[i].add(j)
        trees[j].add(i)
        answer = min(answer, result)
    return answer
        
def dfs(start, trees):
    queue = [start]
    marked = {start}
    while queue:
        v = queue.pop()
        for w in trees[v]:
            if w not in marked:
                queue.append(w)
                marked.add(w)
    
    return len(marked)