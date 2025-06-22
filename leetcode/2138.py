class Solution:
    def divideString(self, s, k, fill):
        ans = []
        for i in range(0, len(s), k):
            ans.append(s[i:i+k])
        if len(ans[-1]) < k:
            ans[-1] += fill * (k - len(ans[-1]))
        return ans
