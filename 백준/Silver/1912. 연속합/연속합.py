import sys
input = sys.stdin.readline


N = int(input().rstrip())
L = list(map(int, (input().rstrip().split(' '))))

for i in range(1, N):
    L[i] = max(L[i], L[i] + L[i-1])

print(max(L))