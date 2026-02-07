class Solution:
    def minimumDeletions(self, s):
        ans = a = s.count('a')
        b = 0
        for c in s:
            b += c == 'b'
            a -= c == 'a'
            ans = min(ans, a + b)
        return ans
