class Solution:
    def minimumPartition(self, s, k):
        if int(max(s)) > k: return -1

        ans, curr = 1, 0
        for x in map(int, s):
            if curr * 10 + x > k:
                ans += 1
                curr = 0
            curr = curr * 10 + x
        return ans
