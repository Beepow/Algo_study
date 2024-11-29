N = int(input())
output = 0
for _ in range(N):
    INPUT = str(input())
    l = set(INPUT)
    if len(INPUT) == len(l) or len(l)==1:
        output += 1
    else:
        cnt, n = 0, 0
        for a in (l):
            if INPUT.count(a) > 1 :
                n += 1
                if len(set(INPUT[INPUT.index(a):INPUT.index(a)+INPUT.count(a)])) ==1:
                    cnt += 1
        if cnt == n:
            output += 1

print(output)