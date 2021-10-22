class Solution:
    def countPalindromicSubsequence(self, s):
        # Count prefix sums and chache last char occurances
        counts, count = [], [0] * 26
        first, last = {}, {}
        for i, c in enumerate(s):
            count[ord(c) - ord('a')] += 1
            counts.append(count.copy())
            last[c] = i
            if c not in first:
                first[c] = i
        count = 0
        # Count the possible palindromes
        for char in first:
            if first[char] != last[char]:
                between =  [a - b for a, b in zip(counts[last[char] - 1], counts[first[char]])]
                count += 26 - between.count(0)
        return count        
