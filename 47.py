class Solution:
    def permuteUnique(self, nums):
        ans, nums = [], sorted(nums)

        def permute(arr, perms, curr=[]):
            if len(curr) == len(nums):
                perms.append(curr[:])
                return
            for i in range(len(arr)):
                if i and arr[i] == arr[i-1]: continue
                curr.append(arr[i])
                permute(arr[:i] + arr[i+1:], perms, curr)
                curr.pop()
                
        permute(nums, ans)
        return ans

