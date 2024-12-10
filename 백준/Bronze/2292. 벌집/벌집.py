N = int(input())-1
i=0
k=1
while 1:
    if N==0:
        k = 0
        break
    elif i*6 < N <= 6*(i+k):
        break
    i += k
    k += 1
print(k+1)
