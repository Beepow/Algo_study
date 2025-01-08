import sys

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

A = dict()
for _ in range(N):
    I = sys.stdin.readline().rstrip()
    if len(I) >= M:
        if I in A:
            A[I] += 1
        else:
            A[I] = 1

output = sorted(A.items(), key = lambda x : (-x[1],-len(x[0]),x[0]))

for i in output:
    print(i[0])