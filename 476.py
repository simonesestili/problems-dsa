class Solution:
    def findComplement(self, num):
        ans = i = 0
        while num:
            ans += int(not num & 1) << i
            num >>= 1
            i += 1
        return ans

