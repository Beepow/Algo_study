import sys
N = int(sys.stdin.readline().rstrip(' '))
stack = []
for _ in range(N):
    A = list(map(int, sys.stdin.readline().rstrip(' ').split(' ')))
    if len(A) == 2:
        stack.append(A[1])
    else:
        B = A[0]
        if B ==2:
            print(stack[-1] if len(stack) !=0 else -1)
            stack.pop() if len(stack) !=0 else 0
        elif B==3:
            print(len(stack))
        elif B==4:
            print(0 if len(stack) else 1)
        elif B==5:
            print(stack[-1] if len(stack) !=0 else -1)
