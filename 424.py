class Solution:
    def characterReplacement(self, s, k):
        count, code = [0] * 26, lambda c: ord(c) - ord('A')

        ans = left = 0
        for right in range(len(s)):
            count[code(s[right])] += 1
            while (right - left + 1) - max(count) > k:
                count[code(s[left])] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans
