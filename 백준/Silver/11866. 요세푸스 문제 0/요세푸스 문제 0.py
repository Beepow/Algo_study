import sys
from collections import deque
N, K = map(int, (sys.stdin.readline().rstrip().split(' ')))

que = deque()
for i in range(N):
    que.append(i+1)
output = []

while que:
    que.rotate(-K+1)
    output.append(str(que.popleft()))

print('<',end='')
print(', '.join(output).rstrip(), end='')
print('>')