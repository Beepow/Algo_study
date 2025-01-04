import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())

que = deque()
for i in range(N):
    que.append(i+1)

while 1:
    if len(que) ==1:
        break
    que.popleft()
    que.append(que.popleft())
print(que[0])