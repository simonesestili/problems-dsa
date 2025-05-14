MOD = 10**9+7
class Solution:
    def lengthAfterTransformations(self, s, t):
        cnts = deque([0] * 26)
        for c in s: cnts[ord(c) - ord('a')] += 1

        for _ in range(t):
            cnts[0] = (cnts[0] + cnts[-1]) % MOD
            cnts.appendleft(cnts.pop())

        return sum(cnts) % MOD
