import sys

A, B = map(int, sys.stdin.readline().split(' '))

def gcd(A, B):
    a, b = max(A, B), min(A, B)
    while a%b:
        a, b = b, a%b
    return b

b = gcd(A, B)

print(A*B//b)