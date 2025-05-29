def minimax(b, turn):
    win_pos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    def win(p): return any(b[i]==b[j]==b[k]==p for i,j,k in win_pos)
    if win('X'): return 1
    if win('O'): return -1
    if ' ' not in b: return 0
    scores = []
    for i in range(9):
        if b[i] == ' ':
            b[i] = turn
            score = minimax(b, 'O' if turn == 'X' else 'X')
            scores.append(score)
            b[i] = ' '
    return max(scores) if turn == 'X' else min(scores)

board = [' '] * 9
print("Minimax Score for empty board:", minimax(board, 'X'))
