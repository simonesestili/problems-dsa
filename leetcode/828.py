class Solution:
    def uniqueLetterString(self, s):
        n = len(s)
        currpre, currsuf = [-1] * 26, [n] * 26
        prefix, suffix = [-1] * n, [-1] * n
        for i in range(n):
            j = n - 1 - i
            prefix[i] = currpre[:]
            suffix[j] = currsuf[:]
            currpre[ord(s[i]) - ord('A')] = i
            currsuf[ord(s[j]) - ord('A')] = j

        count = 0
        for i in range(n):
            v = ord(s[i]) - ord('A')
            count += (i - prefix[i][v]) * (suffix[i][v] - i)
        return count
