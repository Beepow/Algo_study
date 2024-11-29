def convert(grade):
    list = ['F', 'D', 'C', 'B', 'A']
    num = int(grade[0].replace(grade[0], str(list.index(grade[0]))))
    num += 0.5 if grade!='F' and grade[1] == '+' else 0
    return num
res = 0
w=0
for _ in range(20):
    A, score, grade = map(str, input().split(" "))
    if grade != 'P':
        res += float(score) * convert(grade)
        w += float(score)

print(res/w)