import sys
def coord(coordinates):
    for i in set(coordinates):
        if coordinates.count(i)==1:
            return i
        else:
            continue
X = []
Y = []
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split(' '))
    X.append(x)
    Y.append(y)
x_out = coord(X)
y_out = coord(Y)
print(x_out, y_out)