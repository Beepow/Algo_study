import sys

N = sys.stdin.readline().rstrip()

A = set(map(int, sys.stdin.readline().rstrip().split(' ')))

M = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().rstrip().split(' ')))
for b in B:
    print(1 if b in A else 0)