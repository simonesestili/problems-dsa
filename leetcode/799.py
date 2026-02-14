class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        curr = [poured]
        for _ in range(query_row):
            nxt = [0] * (len(curr) + 1)
            for i, x in enumerate(curr):
                rem = max(x - 1, 0)
                nxt[i] += rem / 2
                nxt[i+1] += rem / 2
            curr = nxt
        return min(curr[query_glass], 1)
