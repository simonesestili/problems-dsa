class Solution:
    def equalSubstring(self, s, t, maxCost):
        def cost(a, b):
            return abs(ord(a) - ord(b))

        best = curr = left = 0
        for right in range(len(s)):
            curr += cost(s[right], t[right])
            while curr > maxCost and left <= right:
                curr -= cost(s[left], t[left])
                left += 1
            best = max(best, right - left + 1)
        return best
