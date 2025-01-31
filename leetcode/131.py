class Solution:
    def partition(self, s):
        n = len(s)
        ways = [list() for _ in range(n)]
        for i in range(n - 1, -1, -1):
            if s[i:] == s[i:][::-1]: ways[i].append([s[i:]])
            curr = ''
            for j in range(i, n - 1):
                curr += s[j]
                if curr != curr[::-1]: continue
                for way in ways[j + 1]:
                    ways[i].append([curr] + way)
        return ways[0]
