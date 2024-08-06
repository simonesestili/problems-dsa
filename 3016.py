class Solution:
    def minimumPushes(self, word):
        rem = [4] * 2 + [3] * 8 + [2] * 8 + [1] * 8
        ans, mappings = 0, {}

        for c, cnt in Counter(word).most_common():
            if c not in mappings: mappings[c] = rem.pop()
            ans += mappings[c] * cnt

        return ans

