class Solution:
    # -1: 1 -> 0, -2: 0 -> 1
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        DIRS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        VALS = {-1: 0, -2: 1}

        def alive(i, j):
            return 0 <= i < m and 0 <= j < n and board[i][j] in [1, -1]
        
        def life(i, j):
            neighbors = sum(alive(i+di, j+dj) for di, dj in DIRS)
            lives = 0 if neighbors < 2 or neighbors > 3 else int(board[i][j] or neighbors == 3)
            if board[i][j] == lives: return lives
            return -2 if lives else -1

        for row in range(m):
            for col in range(n):
                board[row][col] = life(row, col)

        for row in range(m):
            for col in range(n):
                if board[row][col] not in VALS: continue
                board[row][col] = VALS[board[row][col]]
