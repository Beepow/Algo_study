T = int(input())
for _ in range(T):
    o = ''
    R, S = map(str, input().split(' '))
    for i in range(len(S)):
        o += S[i]*int(R)
    print(o)