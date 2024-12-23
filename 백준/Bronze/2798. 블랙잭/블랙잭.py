N, M = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
C = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            C = A[i] + A[j] + A[k] if 0 <= M-(A[i] + A[j] + A[k]) < M-C else C
print(C)

