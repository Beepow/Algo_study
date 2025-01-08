import sys

N = int(sys.stdin.readline().rstrip())

def func(n):
    if n > 1:
        return func(n-1) + func(n-2)
    else:
        return n

print(func(N))