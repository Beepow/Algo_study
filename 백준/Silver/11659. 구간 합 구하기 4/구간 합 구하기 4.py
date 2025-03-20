import sys
input = sys.stdin.readline

N, M = map(int, (sys.stdin.readline().rstrip().split(' ')))

A = list(map(int, sys.stdin.readline().rstrip().split(' ')))
S = [0]
tmp = 0

for n in A:
    tmp += n
    S.append(tmp)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split(' '))
    print(S[j]-S[i-1])