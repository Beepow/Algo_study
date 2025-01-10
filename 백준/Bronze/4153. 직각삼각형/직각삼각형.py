import sys

while 1:
    A = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    if sum(A) == 0:
        break

    A.sort()
    if A[0]**2+A[1]**2 == A[-1]**2:
        print('right')
    else:
        print('wrong')


