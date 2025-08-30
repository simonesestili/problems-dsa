class Solution:
    def isValidSudoku(self, board):
        for i in range(9):
            row = [board[i][c] for c in range(9) if board[i][c] != '.']
            col = [board[r][i] for r in range(9) if board[r][i] != '.']
            box = [board[i//3*3+j//3][i%3*3+j%3] for j in range(9) if board[i//3*3+j//3][i%3*3+j%3] != '.']
            if len(row) != len(set(row)): return False
            if len(col) != len(set(col)): return False
            if len(box) != len(set(box)): return False
        return True
