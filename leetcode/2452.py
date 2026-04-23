class Solution:
    def twoEditWords(self, queries, dictionary):
        ans = []
        for q in queries:
            for w in dictionary:
                if sum(a != b for a, b in zip(q, w)) <= 2:
                    ans.append(q)
                    break
        return ans
