import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()  # 작은 번호부터 방문하도록 정렬

# DFS 구현 (재귀)
def dfs(graph, visit, visited):
    visited.append(visit)  # 방문한 노드를 먼저 추가
    for i in graph[visit]:  # 방문 가능한 노드를 순회
        if i not in visited:
            dfs(graph, i, visited)

visited_dfs = []
dfs(graph, V, visited_dfs)
print(" ".join(map(str, visited_dfs)))

# BFS 구현 (큐 활용)
def bfs(graph, start):
    visited_bfs = []
    queue = deque([start])
    visited_bfs.append(start)

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if i not in visited_bfs:
                queue.append(i)
                visited_bfs.append(i)

    print(" ".join(map(str, visited_bfs)))

bfs(graph, V)
