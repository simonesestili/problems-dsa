class Solution:
    def getHappyString(self, n, k):
        total = 2 ** (n - 1)
        if k > 3 * total:
            return ''
        val = (k - 1) // total
        ans = ['a' if not val else 'b' if val == 1 else 'c']
        for _ in range(n - 1):
            k = (k - 1) % total + 1;
            total >>= 1
            val = (k - 1) // total
            if not val:
                ans.append('a' if ans[-1] != 'a' else 'b')
            else:
                ans.append('c' if ans[-1] != 'c' else 'b')
        return ''.join(ans)