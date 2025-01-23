
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().rstrip().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for key in graph:
    graph[key].sort()

visited = [0]*(N+1)
cnt = 1
def dfs(R):
    global cnt
    visited[R] = cnt
    for i in graph[R]:
        if visited[i]==0:
            cnt += 1
            dfs(i)

dfs(R)
print("\n".join(map(str, visited[1:])))
