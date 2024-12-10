import sys
while 1:
    N = int(sys.stdin.readline())
    o = []
    k = ''
    if N == -1:
        break
    else:
        for i in range(1, N):
            o.append(i) if not N%i else 0
        if sum(o) == N:
            print(f'{N} = {" + ".join(str(oo) for oo in o)}')
        else:
            print(f'{N} is NOT perfect.')
