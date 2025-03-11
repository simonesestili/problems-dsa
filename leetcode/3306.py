VOWELS = set('aeiou')
class Solution:
    def solve(self, word, k):
        n, cnts = len(word), defaultdict(int)
        ans = vowels = l = 0
        for r in range(n):
            c = word[r] if word[r] in VOWELS else ''
            vowels += cnts[c] == 0 and c != ''
            cnts[c] += 1
            while vowels == 5 and cnts[''] >= k:
                ans += n - r
                c = word[l] if word[l] in VOWELS else ''
                vowels -= cnts[c] == 1 and c != ''
                cnts[c] -= 1
                l += 1
        return ans

    def countOfSubstrings(self, word, k):
        return self.solve(word, k) - self.solve(word, k + 1)
