import sys
input = sys.stdin.readline

N, M = map(int, (input().rstrip().split()))

def func(x, N, M):
    if len(x) == M:
        print(' '.join(map(str,x)))
        return
    else:
        for i in range(1, N+1):
            if i not in x:
                x.append(i)
                func(x, N, M)
                x.pop()
func([], N, M)