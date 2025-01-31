class Solution:
    def minCharacters(self, a, b):
        acount, bcount = [0] * 26, [0] * 26
        for c in a: acount[ord(c) - ord('a')] += 1
        for c in b: bcount[ord(c) - ord('a')] += 1
        ans = len(a) + len(b) - max(i + j for i, j in zip(acount, bcount))

        for i in range(1, 26):
            acount[i], bcount[i] = acount[i] + acount[i-1], bcount[i] + bcount[i-1]

        for c in range(25):
            cand1 = acount[-1] - acount[c] + bcount[c]
            cand2 = bcount[-1] - bcount[c] + acount[c]
            ans = min(ans, cand1, cand2)

        return ans
