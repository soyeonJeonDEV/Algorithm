#https://programmers.co.kr/learn/courses/30/lessons/43162
#네트워크
def solution(n, computers):
    
    graph = [[] for _ in range(n+1)]
    graph[0] = 0
    visited = [False for _ in range(n+1)]
    cnt = 0
    
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
            else:
                if computers[i][j] == 1:
                    graph[i+1].append(j+1)
                    
    for i in range(1,len(visited)):
        if not visited[i]:
            dfs(graph,i,visited)
            cnt += 1
    return cnt
            
    
def dfs(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)