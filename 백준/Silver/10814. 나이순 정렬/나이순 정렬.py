n=int(input())
l = []
for i in range(n):
    a = list(map(str, input().split()))
    l.append(a)

l.sort(key= lambda x: int(x[0]))

for x, y in l:
    print(x, y)