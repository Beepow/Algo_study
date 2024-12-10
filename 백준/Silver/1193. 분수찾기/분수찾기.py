N = int(input())
k = 1
while N > 0:
    N -= k
    k += 1

if not k%2:
    print(f'{abs(N)+1}/{N+k-1}')
else:
    print(f'{N+k-1}/{abs(N)+1}')