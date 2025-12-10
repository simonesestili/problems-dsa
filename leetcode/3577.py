MOD = 10 ** 9 + 7
class Solution:
    def countPermutations(self, complexity):
        mn = min(complexity)
        if complexity[0] != mn or complexity.count(mn) > 1:
            return 0
        ans = 1
        for i in range(1, len(complexity)):
            ans = (ans * i) % MOD
        return ans
