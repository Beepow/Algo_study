import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = [0]*(N+1)

A[1] = 1
if N > 1:
    A[2] = 2

for i in range(3, N+1):
    A[i] = (A[i-2] + A[i-1])%15746

print(A[N])