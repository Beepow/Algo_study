H, M = map(int, input().split(' '))
C = int(input())
EM = M + C
if EM >= 60:
    H += int(EM/60)
    EM = EM%60
    if H >=24:
        H -= 24
print(H, EM)