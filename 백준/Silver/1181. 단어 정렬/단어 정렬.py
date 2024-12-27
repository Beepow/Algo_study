n=int(input())
l = []
for i in range(n):
    a = input()
    1 if a in l else l.append(a)

l.sort(key= lambda x: (len(x), x))

for i in l:
    print(i)