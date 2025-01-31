class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for row in range(m):
            for col in range(n):
                if self.search(row, col, board, word, 0, set()):
                    return True
        return False        

    def search(self, row, col, board, word, idx, visited):
        if idx == len(word):
            return True
        if (row, col) in visited or row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[idx]:
            return False
        visited.add((row, col))
        return (self.search(row - 1, col, board, word, idx + 1, visited.copy()) or
                self.search(row + 1, col, board, word, idx + 1, visited.copy()) or
                self.search(row, col - 1, board, word, idx + 1, visited.copy()) or
                self.search(row, col + 1, board, word, idx + 1, visited.copy()))
