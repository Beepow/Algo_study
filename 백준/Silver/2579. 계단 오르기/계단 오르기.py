import sys
input = sys.stdin.readline

N = int(input().rstrip())

L = []
for _ in range(N):
    L.append(int(input().rstrip()))
A = [0]*(N+1)

A[1] = L[0]
if N > 1:
    A[2] = L[1] + L[0]

for i in range(3, N+1):
    A[i] = max(L[i-1] + L[i-2] + A[i-3], L[i-1] + A[i-2])

print(A[N])