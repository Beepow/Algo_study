w = list(input().upper())
l = [w.count(i) for i in (set(w))]

if l.count(max(l)) > 1:
    print("?")
else:
    print(list(set(w))[l.index(max(l))])
