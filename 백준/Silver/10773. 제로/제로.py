import sys
K = int(sys.stdin.readline().rstrip(' '))
stack = []

for _ in range(K):
    I = int(sys.stdin.readline().rstrip())
    if I:
        stack.append(I)
    else:
        stack.pop()

print(sum(stack))