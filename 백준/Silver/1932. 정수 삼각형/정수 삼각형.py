import sys
input = sys.stdin.readline


N = int(input().rstrip())
L = []
for n in range(N):
    A = list(map(int, input().rstrip().split(' ')))
    L.append(A)

for i in range(1, N):
    for j in range(i+1):
        if not j:
            L[i][j] = L[i][j] + L[i-1][j]
        elif j == i:
            L[i][j] = L[i][j] + L[i - 1][j-1]
        else:
            L[i][j] = L[i][j] + max(L[i - 1][j - 1], L[i - 1][j])

print(max(L[-1]))