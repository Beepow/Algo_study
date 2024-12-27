N = int(input())

C = set(map(int, input().split(' ')))

M = int(input())

T = list(map(int, input().split(' ')))
output = []
for t in T:
    output.append('1' if t in C else '0')

print(' '.join(output))