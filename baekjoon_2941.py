#https://www.acmicpc.net/problem/2941
#크로아티아 알파벳

n = input()

al = ["c=","c-","dz=","d-","lj","nj","s=","z="]

# answer = 0
# while len(n) > 0:
#     if n[:2] in al:
#         n = n[2:]
#         answer += 1
#     elif n[:3] in al:
#         n = n[3:]
#         answer += 1
#     else:
#         n = n[1:]
#         answer += 1

# print(answer)

for i in al:
    n = n.replace(i,'a')

print(len(n))

