class Solution:
    def stringMatching(self, words):
        return [cand for cand in words if any(cand in w and cand != w for w in words)]
