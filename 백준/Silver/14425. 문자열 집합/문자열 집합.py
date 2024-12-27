N, M = map(int, (input().split(' ')))
S = set()
for _ in range(N):
    S.add(input())
cnt = 0
for _ in range(M):
    cnt += 1 if input() in S else 0
print(cnt)