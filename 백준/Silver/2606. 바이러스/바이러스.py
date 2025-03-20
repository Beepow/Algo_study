import sys
input = sys.stdin.readline

T = int(sys.stdin.readline())
N = int(sys.stdin.readline())

W = [[] for t in range(T+1)]

for n in range(N):
    a, b = map(int, sys.stdin.readline().split(' '))
    W[a].append(b)
    W[b].append(a)

def dfs(graph, visit, visited):
    global cnt
    visited.append(visit)
    for k in graph[visit]:
        if k not in visited:
            cnt += 1
            dfs(graph, k, visited)
visited = []
cnt = 0
dfs(W, 1, visited)

print(cnt)