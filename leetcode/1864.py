class Solution:
    def minSwaps(self, s):
        n, ones = len(s), s.count('1')
        zeros = n - ones
        if abs(ones - zeros) > 1: return -1
        swaps = [0, 0]
        for i in range(0, n, 2):
            swaps[0] += s[i] == '1'
            swaps[1] += s[i] == '0'
        return swaps[0] if zeros > ones else swaps[1] if ones > zeros else min(swaps)
