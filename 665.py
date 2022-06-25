class Solution:
    def checkPossibility(self, nums):
        n, changed = len(nums), False

        for i in range(1, n):
            if nums[i] >= nums[i-1]: continue
            if changed: return False
            changed = True

            if i == 1 or nums[i] >= nums[i-2]:
                nums[i-1] = nums[i]
            else:
                nums[i] = nums[i-1]

        return True
