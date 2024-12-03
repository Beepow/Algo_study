N, M = map(int, input().split(' '))
A, B, S = [], [], []
for i in range(N):
    m1 = list(map(int, input().split(' ')))
    A += m1
for i in range(N):
    m2 = list(map(int, input().split(' ')))
    B += m2
for i in range(N*M):
    s = A[i] + B[i]
    S.append(str(s))
for n in range(N):
    print(' '.join(S[n*M:n*M+M]))