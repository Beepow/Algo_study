def solution(keyinput, board):
    answer = [0, 0]
    h = int((board[1]-1)/2)
    w = int((board[0]-1)/2)
    for i in keyinput:
        if i == 'up':
            if answer[1] == h:
                pass
            else:
                answer[1] += 1
        elif i == 'down':
            if answer[1] == -h:
                pass
            else:
                answer[1] -= 1
        elif i == 'left':
            if answer[0] == -w:
                pass
            else:
                answer[0] -= 1
        elif i == 'right':
            if answer[0] == w:
                pass
            else:
                answer[0] += 1
    return answer