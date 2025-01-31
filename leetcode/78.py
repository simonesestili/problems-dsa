class Solution:
    def subsets(self, nums):
        ans, curr = [], []

        def build(i=0):
            if i == len(nums):
                ans.append(curr[:])
                return

            curr.append(nums[i])
            build(i + 1)
            curr.pop()
            build(i + 1)

        build()
        return ans
