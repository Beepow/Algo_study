import sys

N = int(sys.stdin.readline())

A = set(map(int, sys.stdin.readline().rstrip().split(' ')))

print(max(A)*min(A))