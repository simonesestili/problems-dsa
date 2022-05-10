class Solution:
    def numSplits(self, s):
        left, right = Counter(), Counter(s)
        l, r = 0, len(right.keys())

        count = 0
        for c in s:
            l += left[c] == 0
            left[c] += 1
            right[c] -= 1
            r -= right[c] == 0
            count += l == r

        return count
