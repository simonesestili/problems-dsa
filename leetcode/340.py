class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        ans, code = 0, lambda c: ord(c) - ord('a')
        counts, count = defaultdict(int), 0

        left = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            count += counts[s[right]] == 1
            while count > k:
                counts[s[left]] -= 1
                count -= counts[s[left]] == 0
                left += 1
            ans = max(ans, right - left + 1)

        return ans
