class Solution:
    def gameOfLife(self, board):
        # Calculates next state of given cell
        def life(row, col):
            diffs = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]
            neighbors = 0
            for diff in diffs:
                drow, dcol = row + diff[0], col + diff[1]
                if drow < 0 or dcol < 0 or drow >= len(board) or dcol >= len(board[0]):
                    continue
                neighbors += board[drow][dcol] % 2
            if board[row][col]:
                return 3 if neighbors < 2 or neighbors > 3 else 1
            return 2 if neighbors == 3 else 0

        m, n = len(board), len(board[0])
        # If a dead cell is born mark it as 2
        # If a live cell dies mark it as 3
        for row in range(m):
            for col in range(n):
                board[row][col] = life(row, col)
        # Convert 2s and 3s to 1s and 0s
        for row in range(m):
            for col in range(n):
                val = board[row][col]
                board[row][col] = 1 if val == 2 else 0 if val == 3 else val

