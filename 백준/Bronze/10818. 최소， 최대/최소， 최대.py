N = int(input())
A=[]
s = input().split(' ')
for i in range(N):
    A.append(int(s[i]))
print(min(A), max(A))