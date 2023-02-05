def solution(board):
    n = len(board)
    
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if 0 <= i and i < n and 0 <= j and j < n and board[i][j] == 0:
                            board[i][j] = 2

    return sum(row.count(0) for row in board)