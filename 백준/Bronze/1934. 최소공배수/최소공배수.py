import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split(' '))
    a, b = A, B
    while a % b != 0:
        a, b = b, a % b
    print(A*B//b)