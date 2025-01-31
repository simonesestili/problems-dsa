class Solution:
    def numKLenSubstrNoRepeats(self, s, k):
        code, counts = lambda c: ord(c) - ord('a'), [0] * 26
        ans = uniques = 0
        for i in range(k - 1):
            uniques += counts[code(s[i])] == 0
            counts[code(s[i])] += 1
        for i in range(k - 1, len(s)):
            uniques += counts[code(s[i])] == 0
            counts[code(s[i])] += 1
            ans += uniques == k
            counts[code(s[i - k + 1])] -= 1
            uniques -= counts[code(s[i - k + 1])] == 0
        return ans

