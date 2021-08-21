class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.valid_row(board, i) or not self.valid_col(board, i) or not self.valid_box(board, i):
                return False
        return True

    def valid_row(self, board, row):
        seen = set()
        for col in range(9):
            cell = board[row][col]
            if cell in seen:
                return False
            if cell != '.':
                seen.add(cell)
        return True

    def valid_col(self, board, col):
        seen = set()
        for row in range(9):
            cell = board[row][col]
            if cell in seen:
                return False
            if cell != '.':
                seen.add(cell)
        return True

    def valid_box(self, board, i):
        box_position = ((i // 3) * 3, (i % 3) * 3)
        seen = set()
        for row in range(3):
            for col in range(3):
                cell = board[row + box_position[0]][col + box_position[1]]
                if cell in seen:
                    return False
                if cell != '.':
                    seen.add(cell)
        return True
