import sys

n = int(sys.stdin.readline())
X, Y = [], []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split(' '))
    X.append(x)
    Y.append(y)
print((max(X)-min(X)) * (max(Y)-min(Y)))