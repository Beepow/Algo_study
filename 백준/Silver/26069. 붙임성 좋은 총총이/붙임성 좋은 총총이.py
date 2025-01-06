import sys

N = int(sys.stdin.readline().rstrip())

l = set()

for _ in range(N):
    A, B = map(str, sys.stdin.readline().rstrip().split(' '))

    if A == 'ChongChong':
        l.add(B)
    elif B == 'ChongChong':
        l.add(A)
    elif A in l:
        l.add(B)
    elif B in l:
        l.add(A)

print(len(l)+1)
