def solution(polynomial):
    answer = ''
    cntx=0
    cnt = 0
    d = polynomial.replace('+', '').split()

    for i in d:
        if 'x' in i:
            if i == 'x':
                cntx += 1
            else:
                cntx += int(i[:-1])
        else:
            cnt += int(i)
    
    if cntx == 0:
        return str(cnt)
    elif cntx == 1:
        if cnt == 0:
            return f'x'
        else:
            return f'x + {cnt}'
    else:
        if cnt==0:
            return f'{cntx}x'
        else:
            return f'{cntx}x + {cnt}'
