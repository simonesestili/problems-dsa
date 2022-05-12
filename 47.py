class Solution:
    def permuteUnique(self, nums):
        n, nums = len(nums), sorted(nums)
        self.perms = []

        def permute(arr, curr=[]):
            if len(curr) == n:
                self.perms.append(curr[:])
                return
            for i in range(len(arr)):
                if i and arr[i] == arr[i-1]: continue
                curr.append(arr[i])
                permute(arr[:i] + arr[i+1:], curr)
                curr.pop()
                
        permute(nums)
        return self.perms

