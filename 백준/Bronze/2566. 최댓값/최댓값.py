NUM = []
for _ in range(9):
    NUM += list(map(int, input().split(' ')))
idx = NUM.index(max(NUM))

print(max(NUM))
print(int(idx/9)+1, idx%9 + 1)