class Solution:
    def countDigitOne(self, n):
        ans, prefix, suffix = 0, 0, n
        n, m = [d for d in str(n)], len(str(n))
        for i in range(m):
            places = 10 ** (m - i - 1)
            suffix %= places
            curr = suffix + 1 if n[i] == '1' else 0 if n[i] == '0' else places
            ans += prefix * places + curr
            prefix = prefix * 10 + int(n[i])
        return ans
