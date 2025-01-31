class Solution:
    def reconstructMatrix(self, upper, lower, colsum):
        n = len(colsum)
        ans = [[0] * n for _ in range(2)]

        for i in range(n):
            if colsum[i] == 2:
                ans[0][i] = ans[1][i] = 1
                upper -= 1
                lower -= 1
            elif colsum[i] == 1:
                if upper > lower:
                    ans[0][i] = 1
                    upper -= 1
                else:
                    ans[1][i] = 1
                    lower -= 1

        if upper or lower: return []
        return ans
