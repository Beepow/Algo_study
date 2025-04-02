import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 2D 배열 A 선언 (0으로 초기화)
A = [[0] * (N + 1) for _ in range(N + 1)]

# 입력 및 2D 누적 합 계산
for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, N + 1):
        A[i][j] = row[j - 1] + A[i - 1][j] + A[i][j - 1] - A[i - 1][j - 1]

# M개의 질의 처리
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    # 2D 구간 합 공식
    result = A[x2][y2] - A[x1 - 1][y2] - A[x2][y1 - 1] + A[x1 - 1][y1 - 1]
    
    print(result)
