import sys

def func(n):
    if n == 1:
        return ['*']
    else:
        S = func(n//3)
        L = []
        for s in S:
            L.append(s*3)
        for s in S:
            L.append(s + ' '*(n//3) + s)
        for s in S:
            L.append(s*3)
        return L

while True:
    try:
        N = int(sys.stdin.readline().rstrip())

        output = func(N)
        print('\n'.join(output))

    except:
        break



