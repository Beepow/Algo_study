import sys

S = sys.stdin.readline().rstrip()
l = len(S)
o = set()
for i in range(l):
    for j in range(i+1, l+1):
        o.add(S[i:j])

print(len(o))
