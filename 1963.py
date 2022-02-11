class Solution:
    def minSwaps(self, s):
        swaps = curr = 0
        for c in s:
            curr += 1 if c == '[' else -1
            swaps += curr < 0
            if curr < 0: curr += 2
        return swaps
