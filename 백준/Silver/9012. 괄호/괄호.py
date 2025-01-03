import sys
T = int(sys.stdin.readline().rstrip(' '))
stack = []

for _ in range(T):
    I = list(sys.stdin.readline().rstrip())
    i = 0
    while i< len(I):
        if i + 1 < len(I) and I[i]=='(' and I[i+1]==')':
            I.pop(i+1)
            I.pop(i)
            i = 0
        else:
            i += 1
    print("NO" if I else "YES")