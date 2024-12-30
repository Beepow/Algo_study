N = input().strip()
A = list(map(int, input().split(' ')))
M = input().strip()
B = list(map(int, input().split(' ')))

o = {}
for a in A:
    if a in o:
        o[a] += 1
    else:
        o[a] = 1

for b in B:
  if b in o:
    print(o[b], end=' ')
  else:
     print(0, end=' ')
