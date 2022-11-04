VOWELS = set('aeiouAEIOU')
class Solution:
    def reverseVowels(self, s):
        n, s = len(s), list(s)
        l, r = 0, n - 1
        while True:
            while l < n and s[l] not in VOWELS: l += 1
            while r >= 0 and s[r] not in VOWELS: r -= 1
            if l >= r: break
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
        return ''.join(s)
