class Solution:
    def mostFrequent(self, nums, key):
        n, counts = len(nums), defaultdict(int)

        for i in range(n - 1):
            if nums[i] != key: continue
            counts[nums[i+1]] += 1

        return max(counts, key=lambda val: counts[val])
        
