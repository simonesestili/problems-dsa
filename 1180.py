class Solution:
    def countLetters(self, s):
        prev, count, ans = None, 0, 0
        for c in s:
            if prev != c:
                ans += count * (count + 1) // 2
                prev, count = c, 0
            count += 1
        return ans + count * (count + 1) // 2
