class Solution:
    # 1) Find largest index k such that there is some j > k such that nums[j] > nums[k]
    # 2) Find the index j defined above
    # 3) Swap nums[k] and nums[j]
    # 4) Reverse nums[k + 1:]
    def nextPermutation(self, nums):
        n = len(nums)

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1
        
        for k in range(n - 2, -1, -1):
            if nums[k] < nums[k+1]: break
        else:
            reverse(0, n - 1)
            return

        j = n - 1
        while nums[j] <= nums[k]: j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        reverse(k + 1, n - 1)
