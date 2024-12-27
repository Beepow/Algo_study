n=int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
l.sort()
for x, y in l:
    print(x, y)