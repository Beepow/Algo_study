import sys

A, B = map(int, sys.stdin.readline().rstrip().split(' '))

a, b = max(A,B), min(A,B)
while a%b:
    b1 = b
    b = a%b
    a = b1

print(b)
print(A*B//b)