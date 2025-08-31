class Solution:
    def solveSudoku(self, board):
        rows, cols, boxes = [0] * 9, [0] * 9, [0] * 9
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    rows[r] |= 1 << int(board[r][c])
                    cols[c] |= 1 << int(board[r][c])
                    boxes[r//3*3+c//3] |= 1 << int(board[r][c])

        def dfs(i):
            if i >= len(empty):
                return True
            r, c = empty[i]
            for x in range(1, 10):
                if rows[r] >> x & 1 or cols[c] >> x & 1 or boxes[r//3*3+c//3] >> x & 1:
                    continue
                board[r][c] = str(x)
                rows[r] |= 1 << x
                cols[c] |= 1 << x
                boxes[r//3*3+c//3] |= 1 << x
                if dfs(i+1):
                    return True
                board[r][c] = '.'
                rows[r] -= 1 << x
                cols[c] -= 1 << x
                boxes[r//3*3+c//3] -= 1 << x
            return False

        dfs(0)
