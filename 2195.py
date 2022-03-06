class Solution:
    def minimalKSum(self, nums, k):
        total, nums = 0, sorted(set(nums))
        remove = min(k, nums[0] - 1)
        total += remove * (remove + 1) // 2
        k -= remove
        for i in range(len(nums) - 1):
            if not k: break
            between = nums[i+1] - nums[i] - 1
            remove = min(between, k)
            total += (nums[i] + remove) * (nums[i] + remove + 1) // 2 - nums[i] * (nums[i] + 1) // 2
            k -= remove
        total += (nums[-1] + k) * (nums[-1] + k + 1) // 2 - nums[-1] * (nums[-1] + 1) // 2
        return total
