class Solution:
    def solveNQueens(self, n):
        get_diag = lambda r, c: (r - c + n - 1, r + c)
        ans, board = [], []

        def backtrack(cols=0, diag1=0, diag2=0):
            if len(board) == n:
                ans.append(board[:])
                return
            for i in range(n):
                d1, d2 = get_diag(len(board), i)
                if cols >> i & 1 or diag1 >> d1 & 1 or diag2 >> d2 & 1: continue
                board.append('.' * i + 'Q' + '.' * (n - i - 1))
                backtrack(cols | 1 << i, diag1 | 1 << d1, diag2 | 1 << d2)
                board.pop()
        
        backtrack()
        return ans
