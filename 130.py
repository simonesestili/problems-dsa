class Solution:
        def solve(self, board: List[List[str]]) -> None:
                # Left and Right
                for m in range(len(board)):
                        # Left
                        self.search_border(board, m, 0)
                        # Right
                        self.search_border(board, m, len(board[0]) - 1)

                # Top and Bottom
                for n in range(1, len(board[0]) - 1):
                        # Top
                        self.search_border(board, 0, n)
                        # Bottom
                        self.search_border(board, len(board) - 1, n)

                for row in range(len(board)):
                        for col in range(len(board[0])):
                                if board[row][col] == '-':
                                        board[row][col] = 'O'
                                else:
                                        board[row][col] = 'X'


        def search_border(self, board, row, col):
                if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 'O':
                    return
                board[row][col] = '-'
                self.search_border(board, row + 1, col)
                self.search_border(board, row - 1, col)
                self.search_border(board, row, col + 1)
                self.search_border(board, row, col - 1)

            