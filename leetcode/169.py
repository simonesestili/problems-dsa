class Solution:
    def majorityElement(self, nums):
        cand, delta = None, 0

        for num in nums:
            if not delta: cand = num
            delta += 1 if cand == num else -1

        return cand
