class Solution:
    def lengthOfLongestSubstring(self, s):
        count = defaultdict(int)
        ans = left = 0
        for right in range(len(s)):
            count[s[right]] += 1
            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans
