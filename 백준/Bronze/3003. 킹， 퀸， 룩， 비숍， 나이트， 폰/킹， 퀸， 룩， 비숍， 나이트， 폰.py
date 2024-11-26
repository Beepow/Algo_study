A = [1, 1, 2, 2, 2, 8]
p = input().split(' ')
k = [str(A[i]-int(p[i])) for i in range(6)]
print(' '.join(k))