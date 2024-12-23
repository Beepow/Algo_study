N = int(input())
i = 1
o=0
while(i < N):
    if i+ sum(list(map(int, ' '.join(str(i).split(' '))))) == N:
        o = i
        break
    i += 1

print(o)