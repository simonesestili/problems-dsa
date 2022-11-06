class Solution:
    def minimumMoves(self, s: str) -> int:
        moves = 0
        chars = [letter for letter in s] + ['O', 'O']
        i = 0
        while i < len(s):
            if chars[i] == 'X':
                chars[i], chars[i+1], chars[i+2] = 'O', 'O', 'O'
                moves += 1
                i += 3
            else:
                i += 1

        return moves
