#https://www.acmicpc.net/problem/2798
#블랙잭

n,m = map(int,input().split())

cards = list(map(int,input().split()))
answer = 0

for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            cardSum = cards[i] + cards[j] + cards[k]
            if cardSum > m:
                continue
            else:
                answer = max(answer, cardSum)

print(answer)