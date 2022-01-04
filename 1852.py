class Solution:
    def distinctNumbers(self, nums, k):
        n = len(nums)
        ans, unique, counts = [], 0, defaultdict(int)
        for i in range(k):
            unique += not counts[nums[i]]
            counts[nums[i]] += 1
        for i in range(k, n):
            ans.append(unique)
            unique -= counts[nums[i - k]] == 1
            counts[nums[i - k]] -= 1
            unique += not counts[nums[i]]
            counts[nums[i]] += 1
        ans.append(unique)
        return ans

