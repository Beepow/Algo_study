import sys

T = int(sys.stdin.readline())

for t in range(T):
    M, N = map(int, sys.stdin.readline().rstrip().split(' '))
    n = 1
    k = 1
    for i in range(M):
        n *=N
        k *=(i + 1)
        N -=1
    print(n//k)