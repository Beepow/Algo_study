import sys

N = int(sys.stdin.readline().rstrip())

stack = []
for _ in range(N):
    A = list(sys.stdin.readline().rstrip().split(' '))
    if A[0] == 'push':
        stack.append(A[1])
    elif A[0] == 'pop':
        print(stack.pop() if len(stack) else -1)
    elif A[0] == 'size':
        print(len(stack))
    elif A[0] == 'empty':
        print(0 if len(stack) else 1)
    elif A[0] == 'top':
        print(stack[-1] if len(stack) else -1)
