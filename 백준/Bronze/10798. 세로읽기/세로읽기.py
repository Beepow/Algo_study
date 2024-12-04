s = []
l = 0
for _ in range(5):
    x = list(map(str, input()))
    s.append(x)
    l = len(x) if len(x) > l else l

for k in range(5):
    while(len(s[k])!=l):
        s[k].append('')
output = ''
for i in range(l):
    for j in range(5):
        output += s[j][i]
print(output)