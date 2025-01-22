import sys
input = sys.stdin.readline

N = int(input().rstrip())
NUM = list(map(int, input().rstrip().split()))
OP = list(map(int, input().rstrip().split()))
M = -int(1e9)  # 최댓값
m = int(1e9)   # 최솟값

def func(I, I2):
    global NUM, OP, M, m
    if I == N:
        M = max(M, I2)
        m = min(m, I2)
        return
    else:
        if OP[0]:
            OP[0] -= 1
            func(I + 1, I2 + NUM[I])
            OP[0] += 1
        if OP[1]:
            OP[1] -= 1
            func(I + 1, I2 - NUM[I])
            OP[1] += 1
        if OP[2]:
            OP[2] -= 1
            func(I + 1, I2 * NUM[I])
            OP[2] += 1
        if OP[3]:
            OP[3] -= 1
            # 나눗셈 (C++14 방식 처리)
            if I2 < 0:
                func(I + 1, -(abs(I2) // NUM[I]))
            else:
                func(I + 1, I2 // NUM[I])
            OP[3] += 1

func(1, NUM[0])
print(M)
print(m)
