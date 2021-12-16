class Solution:
    def numWays(self, s):
        n, total, curr, M = len(s), s.count('1'), 0, pow(10, 9) + 7
        if total % 3: return 0
        if not total: return (n - 2) * (n - 1) // 2 % M
        curr = count1 = count2 = 0
        for c in s:
            curr += c == '1'
            count1 += curr == total // 3
            count2 += curr == total // 3 * 2
        return count1 * count2 % M
