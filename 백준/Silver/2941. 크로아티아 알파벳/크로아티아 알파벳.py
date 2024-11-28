w = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for i in cro:
    if i in w:
        cnt += w.count(i)
        w = w.replace(i, " ")
cnt += len(w.replace(' ', ""))
print(cnt)