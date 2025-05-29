def solve_n_queens(board=[], row=0):
    if row == 8: print(board); return
    for col in range(8):
        if all(abs(col - c) != row - r and col != c for r, c in enumerate(board)):
            solve_n_queens(board + [col], row + 1)

solve_n_queens()
