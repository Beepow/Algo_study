import sys

INPUT = sys.stdin

N = int(INPUT.readline().rstrip())

size = list(map(int, INPUT.readline().rstrip().split(' ')))

T, P = map(int, INPUT.readline().rstrip().split(' '))

T_cnt = 0

for i in size:
    T_cnt += i // T
    if i%T != 0:
        T_cnt += 1

print(T_cnt)
print(N//P, N%P)
