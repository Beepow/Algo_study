a, b, c, d, e, f = map(int, input().split(' '))

x = -999
while x < 1000:
    if b != 0:  # b가 0이 아닐 때
        if (c - a * x) % b == 0:  # y가 정수인지 확인
            y = (c - a * x) // b
            if d * x + e * y == f:  # 두 번째 방정식 검증
                break
    else:  # b == 0일 때
        if a == 0:  # a가 0이면 x는 어떤 값도 가능, y만 처리하면 됨
            continue
        if c % a == 0:  # x가 정수인지 확인
            x = c // a
            y = (f - d * x) // e
            if d * x + e * y == f:  # 두 번째 방정식 검증
                break
    x += 1

print(x, y)
