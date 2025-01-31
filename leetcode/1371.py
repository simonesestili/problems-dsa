class Solution:
    def findTheLongestSubstring(self, s):
        VOWELS = 'aeiou'
        ans, seen, curr = 0, {0: -1}, 0
        for i, c in enumerate(s):
            if c in VOWELS: curr ^= 1 << VOWELS.index(c)
            if curr not in seen: seen[curr] = i
            ans = max(ans, i - seen[curr])
        return ans

