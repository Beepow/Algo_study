import sys
from collections import deque
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input().rstrip())

Node = [[] for _ in range(N+1)]
for _ in range(N-1):
    S, E, W = map(int, input().rstrip().split(' '))
    Node[S].append([E, W])
    Node[E].append([S, W])

def Find_Far(start, now):
    for node, weight in Node[start]:
        if visited[node] == -1:
            visited[node] = weight + now
            Find_Far(node, visited[node])

visited = [-1] * (N+1)
visited[1] = 0
Find_Far(1, 0)
start_point = visited.index(max(visited))

visited = [-1] * (N+1)
visited[start_point] = 0
Find_Far(start_point, 0)
print(max(visited))

