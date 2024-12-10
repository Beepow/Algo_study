import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(' ')))
cnt = 0
for a in A:
    t = []
    for k in range(1,a+1):
        t.append(k) if not a%k else 0
    if len(t)==2:
        cnt +=1
print(cnt)