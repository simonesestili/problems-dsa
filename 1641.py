class Solution:
    def countVowelStrings(self, n):
        dp = [1] * 5

        for _ in range(n - 1):
            dp = accumulate(dp)

        return sum(dp)
