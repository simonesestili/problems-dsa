class Solution:
    def containsNearbyDuplicate(self, nums, k):
        indices = defaultdict(int)
        for i, x in enumerate(nums):
            if x in indices and i - indices[x] <= k:
                return True
            indices[x] = i
        return False

