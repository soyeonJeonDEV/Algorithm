#baekjoon_1541 https://www.acmicpc.net/problem/1541
import re

a = input().split('-')

num = []

for i in a:
  count = 0
  s = i.split('+')
  for j in s:
