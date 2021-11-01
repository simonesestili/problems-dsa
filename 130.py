class Solution:
    def solve(self, board):
        m, n = len(board), len(board[0])
        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or board[row][col] != 'O':
                return
            board[row][col] = '.'
            dirs = [[1,0],[0,1],[-1,0],[0,-1]]
            for drow, dcol in dirs:
                dfs(row + drow, col + dcol)
               
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)

        for row in range(m):
            for col in range(n):
                board[row][col] = 'O' if board[row][col] == '.' else 'X'
