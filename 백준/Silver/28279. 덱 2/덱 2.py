import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

que = deque()

for _ in range(N):
    A = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    if A[0] == 1:
        que.appendleft(A[1])
    elif A[0] == 2:
        que.append(A[1])
    elif A[0] ==3:
        print(que.popleft() if que else -1)
    elif A[0] == 4:
        print(que.pop() if que else -1)
    elif A[0] == 5:
        print(len(que))
    elif A[0] == 6:
        print(0 if que else 1)
    elif A[0] == 7:
        print(que[0] if que else -1)
    elif A[0] == 8:
        if que:
            a = que.pop()
            print(a)
            que.append(a)
        else:
            print(-1)
