import sys

N, M = map(int, (sys.stdin.readline().rstrip().split(' ')))

po = dict()
op = dict()

for i in range(N):
    A = sys.stdin.readline().rstrip()
    po[i+1] = A
    op[A] = i+1

for j in range(M):
    I = sys.stdin.readline().rstrip()
    if I.isdigit():
        print(po.get(int(I)))
    else:
        print(op.get(I))