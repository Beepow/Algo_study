import sys
n = []
for _ in range(3):
    n.append(int(sys.stdin.readline()))

if sum(n)==180:
    if len(set(n)) == 1:
        print('Equilateral')
    elif len(set(n)) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
    