class Solution:
    def longestPalindrome(self, s):
        n = len(s)

        def longest(l, r):
            curr = deque()
            while l >= 0 and r < n and s[l] == s[r]:
                if l == r:
                    curr.append(s[l])
                else:
                    curr.appendleft(s[l])
                    curr.append(s[r])
                l -= 1
                r += 1
            return curr

        ans = [s[0]]
        for i in range(n - 1):
            ans = max(ans, longest(i, i), longest(i, i + 1), key=len)

        return ''.join(ans)
