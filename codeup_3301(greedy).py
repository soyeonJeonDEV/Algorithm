#codeup 3301 https://codeup.kr/problem.php?id=3301

array = [50000,10000,5000,1000,500,100,50,10]
n = int(input())
count = 0

for coin in array:
	count += n//coin
	n %= coin
	
print(count)
