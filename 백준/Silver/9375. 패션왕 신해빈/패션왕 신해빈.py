import sys
input = sys.stdin.readline

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    D = dict()
    cnt = 1
    for _ in range(N):
        a, b = map(str, sys.stdin.readline().rstrip().split(' '))
        if b in D:
            D[b].append(a)
        else:
            D[b] = [a]

    for k, v in D.items():
        cnt *= (len(v) + 1)

    print(cnt -1)