class Solution:
    def solve(self, board, word):
        for row in board:
            if word in ''.join(row):
                return True

        for i in range(len(board[0])):
            w = []
            for row in board:
                w.append(row[i])
            if word in ''.join(w):
                return True

        return False
