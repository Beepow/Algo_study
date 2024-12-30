import sys

N, M = map(int, sys.stdin.readline().split(' '))

D = set()
for _ in range(N):
    D.add(sys.stdin.readline().rstrip())
cnt = 0
o = set()
for _ in range(M):
    I = sys.stdin.readline().rstrip()
    if I in D:
        o.add(I)
        cnt += 1
print(cnt)
print('\n'.join(sorted(o)))