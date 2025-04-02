import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, (input().rstrip().split(' ')))
output = 0
while 1:
    if A==B:
        break
    elif A>B:
        output = -2
        break
    else:
        if B%10 == 1:
            B //= 10
        elif B%2 == 0:
            B //= 2
        else:
            output = -2
            break
        output += 1
print(output+1)