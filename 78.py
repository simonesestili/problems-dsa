class Solution:
    def subsets(self, nums):
        self.ans = []
        
        def build(i, curr):
            if i == len(nums):
                self.ans.append(curr[:])
            else:
                build(i + 1, curr)
                build(i + 1, curr + [nums[i]])

        build(0, [])
        return self.ans

class Solution2:
    def subsets(self, nums):
        ans, n = [], len(nums)
        for mask in range(1 << n):
            curr = []
            for i in range(n):
                if (mask >> i) & 1:
                    curr.append(nums[i])
            ans.append(curr)
        return ans
