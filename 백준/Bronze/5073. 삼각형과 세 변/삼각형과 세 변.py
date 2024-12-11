import sys

while 1:
    A = list(map(int, sys.stdin.readline().split(' ')))
    if set(A)=={0}:
        break
    if max(A) >= sum(A)-max(A):
        print('Invalid')
    elif len(set(A))==1:
        print('Equilateral')
    elif len(set(A))==2:
        print('Isosceles')
    else:
        print('Scalene')
