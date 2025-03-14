import sys

input = sys.stdin.readline

X = int(input().rstrip())

c = [0] * (10**6 + 1)

for i in range (2, X+1) :
    c[i] = c[i-1] + 1 

    if i % 2 == 0:
        c[i] = min(c[i], c[i//2] + 1) 
    
    if i % 3 == 0 :
        c[i] = min(c[i], c[i//3] + 1)
    
print(c[X])