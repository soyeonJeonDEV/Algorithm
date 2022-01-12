#https://www.acmicpc.net/problem/4796
#캠핑

i  = 1
while True:
    l, p, v = map(int,input().split())
    rest = p - l
    day = 0

    if l == 0 and p == 0 and v == 0:
        break
    
    while v > 0:
        v -= l
        day += l
        if v > 0:
            v -= rest
        else:
            day += v
    print("Case {}: {}".format(i, day))
    i += 1

