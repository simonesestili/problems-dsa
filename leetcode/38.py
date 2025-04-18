class Solution:
    def countAndSay(self, n):
        curr = '1'
        for _ in range(n - 1):
            curr = ''.join(f'{len(list(cnt))}{c}' for c, cnt in groupby(curr))
        return curr
