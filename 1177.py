class Solution:
    def canMakePaliQueries(self, s, queries):
        n, code = len(s), lambda c: ord(c) - ord('a')
        prefix, curr = [[0] * 26], [0] * 26

        for c in s:
            curr[code(c)] += 1
            prefix.append(curr[:])

        ans = []
        for left, right, k in queries:
            delta = [(r - l) & 1 for l, r in zip(prefix[left], prefix[right+1])]
            ans.append(self.validate(delta, k))
        return ans

    def validate(self, counts, k):
        return sum(counts) // 2 <= k
        
