import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

A, B, C = map(int, input().split())

def power(a,b,c):
    if b==0:
        return 1
    half = power(a,b//2,c)
    if b % 2:
        return (half*half*a)%c
    else:
        return (half*half)%c
print(power(A,B,C))