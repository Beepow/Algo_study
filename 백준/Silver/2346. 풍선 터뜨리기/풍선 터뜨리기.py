import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
que = deque(enumerate(map(int, sys.stdin.readline().rstrip().split(' '))))

output = []
for _ in range(N):
    (i, a) = que.popleft()
    output.append(str(i+1))
    que.rotate(-a+1 if a >0 else -a)
print(' '.join(output))
