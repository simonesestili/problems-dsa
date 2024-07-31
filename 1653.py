class Solution:     
    def minimumDeletions(self, s):
        arem, brem = s.count('a'), 0
        ans = arem
        for c in s:
            if c == 'a': arem -= 1
            else: brem += 1
            ans = min(ans, arem + brem)
        return ans

