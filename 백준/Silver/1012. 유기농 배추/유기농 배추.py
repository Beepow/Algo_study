import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip())


def check(B, m, n):
    if m < 0 or m >= M or n < 0 or n >= N:
        return
    if B[n][m] == 0:
        return
    B[n][m] = 0
    check(B, m + 1, n)
    check(B, m - 1, n)
    check(B, m, n + 1)
    check(B, m, n - 1)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(B, m, n):
    queue = deque([(m, n)])
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N and B[ny][nx] == 1:
                B[ny][nx] = 0  # 방문 처리
                queue.append((nx, ny))


for _ in range(T):
    M, N, K = map(int, input().rstrip().split(' '))
    B = [[0 for _ in range(M)] for _ in range(N)]
    for k in range(K):
        x, y = map(int, input().rstrip().split(' '))
        B[y][x] = 1

    cnt = 0
    for m in range(M):
        for n in range(N):
            if B[n][m]:
                bfs(B, m, n)
                cnt += 1
    print(cnt)