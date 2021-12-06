class Solution:
    def findPairs(self, nums, k):
        if not k:
            counter = Counter(nums)
            return len([num for num in counter if counter[num] >= 2]) 
        nums = set(nums)
        freq, count = defaultdict(int), 0
        for num in nums:
            count += freq[num - k] + freq[num + k]
            freq[num] += 1
        return count
