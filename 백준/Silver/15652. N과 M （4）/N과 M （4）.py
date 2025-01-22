import sys
input = sys.stdin.readline

N, M = map(int, (input().rstrip().split()))
o = []
def func(s):
    if len(o) == M:
        print(' '.join(map(str, o)))
        return
    else:
        for i in range(s, N+1):
            o.append(i)
            func(i)
            o.pop()

func(1)