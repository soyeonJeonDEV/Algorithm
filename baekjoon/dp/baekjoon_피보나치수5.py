n = int(input())

p = [0,1]

for i in range(2,21):
  p.append(p[i-1] +p[i-2])

print(p[n])