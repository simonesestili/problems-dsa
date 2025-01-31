class Solution:
    def isValidSudoku(self, board):
        for row in range(9):
            seen = set()

