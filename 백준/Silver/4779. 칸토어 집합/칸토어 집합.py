import sys

def func(s, n):
    s[(3**(n-1)):(3**(n-1))*2] = ' '*(3**(n-1))
    if n==1:
        return s
    else:
        return func(s[0:(3**(n-1))], n - 1) +s[(3**(n-1)):(3**(n-1))*2]+ func(s[(3**(n-1))*2:], n-1)

while True:
    try:
        N = int(sys.stdin.readline().rstrip())
        S = ['-']*(3**N)
        if N:
            output = func(S, N)
            print(''.join(output))
        else:
            print('-')


    except:
        break



