class Solution:
    def winnerOfGame(self, colors):
        acount, bcount, A, B = 0, 0, 'A', 'B'
        curr, prev = 0, '!'
        for col in (colors + '!'):
            if col != prev:
                if prev == A: acount += max(0, curr - 2)
                else: bcount += max(0, curr - 2)
                curr, prev = 0, col
            curr += 1
        return acount > bcount

