class Solution:
    def majorityElement(self, nums):
        majors, n = set(), len(nums)
        for _ in range(16):
            num = nums[randint(0, n - 1)]
            if nums.count(num) > n / 3:
                majors.add(num)
        return list(majors)
