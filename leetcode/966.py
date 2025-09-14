class Solution:
    def spellchecker(self, wordlist, queries):
        def v(s):
            return ''.join('*' if c in 'aeiou' else c for c in s.lower())

        normal, caps, vowels = {}, {}, {}
        for w in reversed(wordlist):
            normal[w] = w
            caps[w.lower()] = w
            vowels[v(w)] = w

        return [normal.get(w) or caps.get(w.lower()) or vowels.get(v(w)) or '' for w in queries]
