class Solution:
    def waysToMakeFair(self, nums):
        ans, n = 0, len(nums)
        sufeven, sufodd = sum(nums[i] for i in range(0, n, 2)), sum(nums[i] for i in range(1, n, 2))
        preeven = preodd = 0
        
        for i in range(n):
            if i & 1: sufodd -= nums[i]
            else: sufeven -= nums[i]
            ans += preeven + sufodd == preodd + sufeven
            if i & 1: preodd += nums[i]
            else: preeven += nums[i]

        return ans
