vowels = 'AEIOUaeiou'
vowel_idx = {c: i for i, c in enumerate(vowels)}
class Solution:
    def sortVowels(self, s):
        cnts = [0] * 10
        for c in s:
            if c in vowel_idx:
                cnts[vowel_idx[c]] += 1

        s, v = list(s), 0
        for i, c in enumerate(s):
            if c in vowel_idx:
                while cnts[v] == 0: v += 1
                s[i] = vowels[v]
                cnts[v] -= 1

        return ''.join(s)
