#연구소
#https://www.acmicpc.net/problem/14502
#3단계
#1단계: 주어진 연구소에서 3개의 벽을 선택한다 => 조합(combinations) 사용
#2단계: 벽이 선택된 연구소에 바이러스를 퍼트린다 => bfs or dfs 사용
#3단계: 바이러스가 퍼지지 않은 안전지역 갯수를 구한다
#https://mentha2.tistory.com/24 다음에 공부

import copy
import sys

input = sys.stdin.readline

n,m = map(int,input().strip().split())
nm = []

for i in range(n):
  l = list(map(int,input().strip().split()))
  nm.append(l)

dr = [-1,0,1,0]
dc = [0,1,0,-1]

max_value = 0

def select_wall(start,count):
  global max_value
  if count == 3:
    sel_nm = copy.deepcopy(nm)