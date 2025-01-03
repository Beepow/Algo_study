import sys
N = int(sys.stdin.readline().rstrip())

L = list(map(int, sys.stdin.readline().split(' ')))
i=1
tmp = []

while L or tmp:
    if tmp:
        if not L and tmp[-1] !=i:
            break
        elif tmp[-1] == i:
            tmp.pop()
            i += 1
        elif L[0] == i:
            L.pop(0)
            i += 1
        else:
            tmp.append(L.pop(0))
    else:
        if L[0] == i:
            L.pop(0)
            i += 1
        else:
            tmp.append(L.pop(0))

print("Nice" if not tmp else "Sad")