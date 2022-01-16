class Solution:
    def divideString(self, s, k, fill):
        s += fill * (-len(s) % k)
        return [s[i:i+k] for i in range(0, len(s), k)]
