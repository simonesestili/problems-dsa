class Solution:
    def isZeroArray(self, nums, queries):
        delta = defaultdict(int)
        for l, r in queries:
            delta[l] += 1
            delta[r+1] -= 1

        curr = 0
        for i, x in enumerate(nums):
            curr += delta[i]
            if x > curr:
                return False

        return True
