import sys

N = int(sys.stdin.readline().rstrip())

que = []
for _ in range(N):
    A = list(sys.stdin.readline().rstrip().split(' '))
    if A[0] == 'push':
        que.append(A[1])
    elif A[0] == 'pop':
        print(que.pop(0) if len(que) else -1)
    elif A[0] == 'size':
        print(len(que))
    elif A[0] == 'empty':
        print(0 if len(que) else 1)
    elif A[0] == 'back':
        print(que[-1] if len(que) else -1)
    elif A[0] == 'front':
        print(que[0] if len(que) else -1)
