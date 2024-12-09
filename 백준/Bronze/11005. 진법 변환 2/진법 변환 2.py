N, B = map(int, input().split(' '))
A = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
O = ''
while N >= B:
    O += A[N%B]
    N = N // B
O += A[N]

print(O[::-1])