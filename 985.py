class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        ans, total = [], sum(x for x in nums if x % 2 == 0)
        for val, idx in queries:
            if nums[idx] % 2 == 0: total -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0: total += nums[idx]
            ans.append(total)
        return ans
