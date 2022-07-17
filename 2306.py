class Solution:
    def distinctNames(self, ideas):
        suffixs = [set() for _ in range(26)]
        for idea in ideas: suffixs[ord(idea[0]) - ord('a')].add(idea[1:])

        count = 0
        for a in range(1, 26):
            for b in range(a):
                overlap = len(suffixs[a] & suffixs[b])
                count += (len(suffixs[a]) - overlap) * (len(suffixs[b]) - overlap)

        return count * 2
