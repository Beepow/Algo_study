import sys

def func(input):
    for i in range(int(len(input)/2)):
        if input[i] != input[-i-1]:
            return print('no')
        else:
            continue
    return print("yes")

while 1 :
    A = sys.stdin.readline().rstrip()
    if A == '0':
        break
    func(A)

