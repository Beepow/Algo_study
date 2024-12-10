A, B, V = map(int, input().split(' '))
i=1
V -= A
i += V//(A-B)
i += 1 if V%(A-B) else 0
print(i)