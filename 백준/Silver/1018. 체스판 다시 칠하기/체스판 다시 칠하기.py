N, M = map(int, input().split(' '))
l1 = []
for _ in range(N):
    l1.append(input())
S1, S2 = 0, 0
cnt = N*M
def board(x, y):
    l2 = []
    for i in range(x, x+8):
        l2.append(l1[i][y:y+8])
    return l2

def color(board):
    cnt_B = 0
    cnt_W = 0
    start = board[0][0]
    for j in range(8):
        for k in range(8):
            cnt_B += 1 if (j+k)%2 and board[j][k]==start else 0
            cnt_B += 1 if not (j + k) % 2 and board[j][k]!=start else 0
            cnt_W += 1 if (j+k)%2 and board[j][k]!=start else 0
            cnt_W += 1 if not (j + k) % 2 and board[j][k]==start else 0
    return min(cnt_W,cnt_B)

while(1):
    new_board = board(S1, S2)
    new_cnt = color(new_board)
    if new_cnt < cnt:
        cnt = new_cnt
    if S1+8==N and S2+8==M:
        print(cnt)
        break
    elif S2+8 == M:
        S2 = 0
        S1 += 1
    else:
        S2 += 1


