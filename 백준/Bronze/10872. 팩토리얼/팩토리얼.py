import sys

N = int(sys.stdin.readline().rstrip())

O = 1
for i in range(N):
    O *= (i+1)
print(O)