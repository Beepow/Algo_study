alpha = ['-1'] *26
S = input()
for i, s in enumerate(S):
    if alpha[ord(s)-ord('a')] == '-1':
        alpha[ord(s)-ord('a')] = str(i)
    else:
        pass
print(' '.join(alpha))