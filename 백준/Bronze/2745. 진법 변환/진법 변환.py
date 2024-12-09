N, B = map(str, input().split(' '))
O = 0
for i, n in enumerate(N[::-1]):
    if 47 < ord(n) < 58:
        O += (ord(n)-48)*(int(B)**i)
    else:
        O += (ord(n) - 55)*(int(B)**i)
print(O)