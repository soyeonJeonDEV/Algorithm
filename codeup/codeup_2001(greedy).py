#codeup_2001 https://codeup.kr/problem.php?id=2001

pasta=[]
for i in range(3):
	pasta.append(float(input()))
juice=[]
for i in range(2):
	juice.append(float(input()))

p1 = min(pasta)
j1 = min(juice)

price = (p1+j1)*1.1

print("%.1f"%price)
