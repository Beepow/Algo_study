import sys

N = int(sys.stdin.readline().rstrip())

def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)

print(fact(N) if N else 1)