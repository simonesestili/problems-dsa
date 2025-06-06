class Solution:
    def robotWithString(self, s):
        cnts, s, t = Counter(s), list(s[::-1]), []

        ans = []
        while s or t:
            if not t or any(cnts[c] > 0 and c < t[-1] for c in string.ascii_lowercase):
                cnts[s[-1]] -= 1
                t.append(s.pop())
            else:
                ans.append(t.pop())

        return ''.join(ans)
