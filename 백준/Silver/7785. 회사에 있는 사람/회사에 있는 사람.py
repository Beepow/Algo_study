N = int(input())
S = set()
for _ in range(N):
    name, a = map(str, input().split(' '))
    if a == 'enter':
        S.add(name)
    else:
        S.discard(name)

for s in sorted(S)[::-1]:
    print(s)