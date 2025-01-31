class Solution:
    def minDominoRotations(self, a, b):

        def solve(main, aux, target):
            moves = 0
            for i in range(len(main)):
                if main[i] == target: continue
                elif aux[i] == target: moves += 1
                else: return float('inf')
            return moves

        fulltop = min(solve(a, b, a[0]), solve(a, b, b[0]))
        fullbot = min(solve(b, a, a[0]), solve(b, a, b[0]))
        ans = min(fulltop, fullbot)
        return -1 if ans == float('inf') else ans
