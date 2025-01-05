import sys

N, K = map(int, sys.stdin.readline().rstrip().split(' '))

n = 1
k = 1
for i in range(K):
    n *=N
    k *=(i + 1)
    N -=1
print(n//k)