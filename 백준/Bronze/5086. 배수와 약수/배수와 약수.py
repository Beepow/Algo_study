import sys
while 1:
    a,b = map(int, (sys.stdin.readline().split(' ')))
    if a == b ==0:
        break
    elif a>b and not a%b:
        print('multiple')
    elif a < b and not b%a:
        print('factor')
    else:
        print('neither')
