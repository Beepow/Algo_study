import sys

N = int(sys.stdin.readline().rstrip())
f = [0] * (N + 1)
cnt1 = cnt2 = 0

def fib(n):
    f[1] = f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


print(fib(N), N-2)
