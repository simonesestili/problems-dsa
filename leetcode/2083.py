class Solution:
    def numberOfSubstrings(self, s):
        count, prev = 0, [0] * 26
        for c in s:
            prev[ord(c) - ord('a')] += 1
            count += prev[ord(c) - ord('a')]
        return count
