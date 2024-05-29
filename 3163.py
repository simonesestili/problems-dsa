class Solution:
    def compressedString(self, w):
        ans, prev, count = [], w[0], 0
        for c in w + '!':
            if c != prev or count == 9:
                ans.append(f'{count}{prev}')
                prev, count = c, 0
            count += 1
        return ''.join(ans)

