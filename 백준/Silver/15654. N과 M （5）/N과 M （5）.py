import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num = sorted(num)
out = []

def BT(out):
    if len(out) == M:
        print(' '.join(out))
        return out.pop()
    for i in range(N):
        if str(num[i]) not in out:
            out.append(str(num[i]))
            BT(out)
    out.pop() if len(out) else 0
BT(out)
