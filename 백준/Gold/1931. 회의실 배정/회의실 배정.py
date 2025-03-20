import sys
input = sys.stdin.readline

N = int(input().rstrip())
startandend = []

for _ in range(N):
    startandend.append(list(map(int, input().rstrip().split(' '))))

startandend.sort(key=lambda x: (x[1],x[0]))

s = 0
cnt = 0

for se in startandend:
    if se[0] >= s:
        s = se[1]
        cnt += 1
print(cnt)