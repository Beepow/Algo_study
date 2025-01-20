import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    A = [0]*(N+1)

    A[1] = 1
    if N > 1:
        A[2] = 1
    if N > 2:
        A[3] = 1
    if N > 3:
        A[4] = 2
    if N > 4:
        A[5] = 2

    for i in range(6, N+1):
        A[i] = (A[i-5] + A[i-1])
    print(A[N])