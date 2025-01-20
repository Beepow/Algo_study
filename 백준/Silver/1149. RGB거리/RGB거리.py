import sys
input = sys.stdin.readline


N = int(input().rstrip())
L = []
for _ in range(N):
    R,G,B = map(int, input().rstrip().split(' '))
    L.append([R,G,B])
A = [[0] * 3 for _ in range(N)]

for i in range(0, N):
    A[i][0] = min(A[i-1][1], A[i-1][2]) + L[i][0]
    A[i][1] = min(A[i-1][0], A[i-1][2]) + L[i][1]
    A[i][2] = min(A[i-1][1], A[i-1][0]) + L[i][2]
print(min(A[-1]))