class Solution:
    def minDeletionSize(self, strs):
        return sum(any(strs[i][c] < strs[i-1][c] for i in range(1, len(strs))) for c in range(len(strs[0])))
