class Solution:
    def getLucky(self, s, k):
        s = ''.join(str(ord(c) - ord('a') + 1) for c in s)

        for _ in range(k):
            s = str(sum(int(c) for c in s))

        return int(s)
