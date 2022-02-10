class Solution:
    def getModifiedArray(self, length, updates):
        delta = defaultdict(int)
        for start, end, inc in updates:
            delta[start] += inc
            delta[end + 1] -= inc

        ans = [0] * length
        for i in range(length):
            prev = ans[i - 1] if i else 0
            ans[i] = delta[i] + prev

        return ans
