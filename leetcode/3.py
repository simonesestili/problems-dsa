class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = set()
        ans = left = 0
        for right, right_char in enumerate(s):
            while right_char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(right_char)
            ans = max(ans, right - left + 1)
        return ans
