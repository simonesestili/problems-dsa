class Solution:
    def findNumOfValidWords(self, words, puzzles):
        # Precompute a map which holds the counts of certian word occurances in the form of their bitmask
        counts = defaultdict(int)
        for word in words:
            counts[self.get_mask(word)] += 1
        ans = [0] * len(puzzles)
        # For each puzzle count the number of valid words
        for i, puzzle in enumerate(puzzles):
            mask = submask = self.get_mask(puzzle)
            first = 1 << (ord(puzzle[0]) - ord('a'))
            # Check for all combinations of submasks possible
            while submask:
                if (submask & first):
                    ans[i] += counts[submask]
                submask = (submask - 1) & mask
        return ans

    def get_mask(self, word):
        mask = 0
        for c in word:
            mask |= 1 << (ord(c) - ord('a'))
        return mask
