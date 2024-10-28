N, X = map(int, input().split(' '))
A = input().split(' ')
output = ''
for i in range(N):
    if int(A[i]) < X:
        output += A[i] + ' '
print(output.rstrip())