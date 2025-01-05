class Solution:
    def shiftingLetters(self, s, shifts):
        delta = [0] * (len(s) + 1)
        for l, r, d in shifts:
            delta[l] += 1 if d else -1
            delta[r+1] -= 1 if d else -1
        ans, d = [], 0
        for i, c in enumerate(s):
            d += delta[i]
            ans.append(chr((ord(c) - ord('a') + d) % 26 + ord('a')))
        return ''.join(ans)
