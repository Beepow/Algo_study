import sys
input = sys.stdin.readline


N = int(input().rstrip())

L = [int(input().rstrip()) for _ in range(N)]
L.insert(0, 0)

E = [0] * (N+1)
E[1] = L[1]
if N > 1:
    E[2] = L[1] + L[2]

for i in range(3, N+1):
    E[i] = max(E[i-1], E[i-2] + L[i], L[i] + L[i-1] + E[i-3])

print(E[-1])