class Solution:
    def nearestPalindromic(self, s):
        n = len(s)

        if n == 1:
            return str(int(s) - 1)

        cands = []
        half = s[:(n+1)//2]

        cands.append('1' + '0' * (n - 1) + '1')
        cands.append('9' * (n - 1))
        cands.append('9' * (n - 1))
        cands.append(str(int(half)-1) + str(int(half)-1)[-1-n%2::-1])
        cands.append(half + half[-1-n%2::-1])
        cands.append(str(int(half)+1) + str(int(half)+1)[-1-n%2::-1])

        def delta(x):
            return abs(int(s) - int(x)), int(x)

        return min([cand for cand in cands if cand != s and cand == cand[::-1]], key=delta)
