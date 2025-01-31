class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        def is_arithmetic(left, right):
            if right - left <= 0: 
                return False
            subarr = sorted(nums[left:right + 1])
            diff = subarr[1] - subarr[0]
            for i in range(right - left):
                if subarr[i + 1] - subarr[i] != diff:
                    return False
            return True

        return [is_arithmetic(l[i], r[i]) for i in range(len(l))]
