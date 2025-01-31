class Solution:
    def longestStrChain(self, words):
        chains = {}

        for w in sorted(words, key=len):
            chains[w] = 1 + max(chains.get(w[:i] + w[i+1:], 0) for i in range(len(w)))

        return max(chains.values())
