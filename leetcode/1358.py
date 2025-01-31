class Solution:
    def numberOfSubstrings(self, s):
        prev, count = [-1, -1, -1], 0
        for i, x in enumerate(s):
            prev[ord(x) - ord('a')] = i
            count += min(prev) + 1
        return count
