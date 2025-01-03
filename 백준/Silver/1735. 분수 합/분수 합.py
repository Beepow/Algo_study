import sys

A1, B1 = map(int, sys.stdin.readline().split(' '))
A2, B2 = map(int, sys.stdin.readline().split(' '))

def gcd(A, B):
    a, b = max(A, B), min(A, B)
    while a%b:
        a, b = b, a%b
    return b

b = gcd(B1, B2)
outB = B1*B2//b

outA = (A1*(outB//B1)) + (A2*(outB//B2))
C = gcd(outA, outB)
print(outA//C, outB//C)