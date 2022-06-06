class Solution:
    def totalNQueens(self, n):
        get_diag1 = lambda r, c: r - c + n - 1
        get_diag2 = lambda r, c: r + c

        def count(curr_row=0, col=0, diag1=0, diag2=0):
            if curr_row == n: return 1
            total = 0
            for i in range(n):
                d1, d2 = get_diag1(curr_row, i), get_diag2(curr_row, i)
                if col >> i & 1 or diag1 >> d1 & 1 or diag2 >> d2 & 1: continue
                total += count(curr_row + 1, col | 1 << i, diag1 | 1 << d1, diag2 | 1 << d2)
            return total

        return count()
