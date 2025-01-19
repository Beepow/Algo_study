import sys

input = sys.stdin.readline

N, M = map(int, sys.stdin.readline().rstrip().split(' '))
L = dict()
for _ in range(N):
    A, B = map(str, input().rstrip().split(' '))
    L[A] = B

for _ in range(M):
    S = input().rstrip()
    print(L[S])