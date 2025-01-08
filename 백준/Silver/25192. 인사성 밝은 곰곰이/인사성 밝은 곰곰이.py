import sys

N = int(sys.stdin.readline().rstrip())

C = set()
cnt = 0
for _ in range(N):
    I = sys.stdin.readline().rstrip()
    if I == 'ENTER':
        cnt += len(C)
        C.clear()
    else:
        C.add(I)
cnt += len(C)
print(cnt)