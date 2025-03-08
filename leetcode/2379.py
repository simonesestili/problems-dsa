class Solution:
    def minimumRecolors(self, blocks, k):
        ans, curr = inf, sum(c == 'W' for c in blocks[:k-1])
        for i in range(k - 1, len(blocks)):
            curr += blocks[i] == 'W'
            ans = min(ans, curr)
            curr -= blocks[i - k + 1] == 'W'
        return ans
