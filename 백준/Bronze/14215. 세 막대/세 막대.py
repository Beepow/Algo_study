import sys

A = list(map(int, sys.stdin.readline().split(' ')))

if max(A)>=sum(A)-max(A):
    print(2*(sum(A)-max(A)) - 1)
else:
    print(sum(A))