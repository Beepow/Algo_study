import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, (input().rstrip().split(' ')))
graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def find(L, sx, sy):
    queue = deque()
    queue.append((sx, sy))
    while queue:
        x, y = queue.popleft()
        if x == N - 1 and y == M - 1:
            return L[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue

            if L[nx][ny]==1:
                L[nx][ny] = L[x][y]+1
                queue.append((nx,ny))
    return -1
print(find(graph, 0, 0))
