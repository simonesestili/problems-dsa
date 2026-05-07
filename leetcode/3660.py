class Solution:
    def maxValue(self, nums):
        n, pref, suff = len(nums), nums[:], nums[:]
        for i in range(1, n):
            pref[i] = max(pref[i], pref[i-1])
            suff[-1-i] = min(suff[-1-i], suff[-i])

        ans = pref[:]
        for i in range(n-2, -1, -1):
            if pref[i] > suff[i+1]:
                ans[i] = ans[i+1]

        return ans
