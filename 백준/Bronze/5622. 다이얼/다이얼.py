Dial = '33344455566677788889991111'
S = input()
t=0
for i in S:
    if int(Dial[ord(i)-ord('A')])==1:
        t += 10
    else:
        t += int(Dial[ord(i)-ord('A')])
print(t)