class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums.copy()
        self.nums = nums.copy()
    
    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n):
            j = random.randint(0, n - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums    
