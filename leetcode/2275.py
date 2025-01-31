class Solution:
    def largestCombination(self, arr):
        positions = [0] * int(log2(max(arr)) + 1)
        for x in arr:
            for i in range(len(positions)):
                if x == 0: break
                positions[i] += x & 1
                x >>= 1
        return max(positions)
