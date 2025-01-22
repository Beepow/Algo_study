import sys
input = sys.stdin.readline

N, M = map(int, (input().rstrip().split()))
o = []
def func():
    if len(o) == M:
        print(' '.join(map(str, o)))
        return
    else:
        for i in range(1, N+1):
            o.append(i)
            func()
            o.pop()

func()