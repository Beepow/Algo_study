import sys
N = int(sys.stdin.readline())
o = []
if N == 1:
    pass
else:
    while N > 1:
        for i in range(2, N+1):
            if not N%i:
                o.append(i)
                break
            else:
                continue
        N //= o[len(o)-1]
for ii in o:
    print(ii)
