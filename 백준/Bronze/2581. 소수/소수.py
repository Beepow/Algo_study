import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
oo = []
for i in range(M, N+1):
    o = []
    for j in range(2, i+1):
        o.append(j) if not i%j else 0
    if len(o)==1:
        oo.append(i)
if len(oo):
    print(sum(oo))
    print(min(oo))
else:
    print(-1)