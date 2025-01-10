import sys

N = int(sys.stdin.readline().rstrip())


A = list(map(int, sys.stdin.readline().rstrip().split(' ')))
A.sort(reverse=True)
T = 0
t = 0
for i in range(N):
    t += A.pop()
    T += t
print(T)

