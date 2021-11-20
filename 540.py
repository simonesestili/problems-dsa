class Solution:
    def singleNonDuplicate(self, nums):
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid - 1] == nums[mid]:
                if (right - mid) % 2:
                    left = mid + 1
                else:
                    right = mid - 2
            elif nums[mid] == nums[mid + 1]:
                if (right - mid - 1) % 2:
                    left = mid + 2
                else:
                    right = mid - 1
            else:
                return nums[mid]

        return nums[left]
