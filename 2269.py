class Solution:
    def divisorSubstrings(self, num, k):
        s = str(num)
        count, curr = 0, 0 if k == 1 else int(s[:k-1])
        for i in range(k - 1, len(s)):
            curr = curr * 10 + int(s[i])
            count += curr and not num % curr
            curr %= pow(10, k - 1)
        return count
