a,b,c = map(int, input().split(' '))

if a==b:
    if a==c:
        print(a*1000 + 10000)
    else:
        print(a*100+1000)
elif b==c:
    print(b*100 + 1000)
elif a==c:
    print(a*100 + 1000)
else:
    print(max(a,b,c)*100)