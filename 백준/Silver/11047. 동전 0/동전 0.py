import sys

input = sys.stdin.readline

N, K = map(int, sys.stdin.readline().rstrip().split(' '))
Money = []
for _ in range(N):
    A = int(sys.stdin.readline().rstrip(' '))
    Money.append(A)

Money = Money[::-1]

c = 0
for m in Money:
    c += K//m
    K %= m

print(c)