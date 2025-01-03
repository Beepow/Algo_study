import sys
def gcd(A, B):
    a, b = max(A, B), min(A, B)
    while a%b:
        a, b = b, a%b
    return b

N = int(sys.stdin.readline().rstrip())
T1 = int(sys.stdin.readline().rstrip())
l = []
for _ in range(N-1):
    T = int(sys.stdin.readline().rstrip())
    l.append(T-T1)
    T1 = T

d = l[0]
for i in range(1,len(l)):
    d = gcd(d, l[i])
cnt = 0
for j in l:
    cnt += j//d - 1
print(cnt)


