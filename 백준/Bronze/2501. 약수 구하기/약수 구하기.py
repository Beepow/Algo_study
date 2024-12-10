import sys
N, K = map(int, sys.stdin.readline().split(' '))
o = []
for i in range(1, N+1):
    o.append(i) if not N%i else 0
print(o[K-1] if len(o)>=K else 0)