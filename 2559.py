VOWELS = 'aeiou'
class Solution:
    def vowelStrings(self, words, queries):
        prefix, curr = [0], 0
        for w in words:
            curr += w[0] in VOWELS and w[-1] in VOWELS
            prefix.append(curr)
        ans = []
        for l, r in queries:
            ans.append(prefix[r+1] - prefix[l])
        return ans
