import sys

N = int(sys.stdin.readline().rstrip())

S = set()
l = set(range(1, 21))
for _ in range(N):
    A = list(sys.stdin.readline().rstrip().split(' '))
    if A[0] == 'add':
        S.add(int(A[1]))
    elif A[0] == 'remove':
        S.discard(int(A[1]))
    elif A[0] == 'check':
        print(1 if int(A[1]) in S else 0)
    elif A[0] == 'toggle':
        S.discard(int(A[1])) if int(A[1]) in S else S.add(int(A[1]))
    elif A[0] == 'all':
        S = l.copy()
    elif A[0] == 'empty':
        S.clear()
