class Solution:
    def maximumSum(self, arr):
        ans = zero = one = float('-inf')
        for num in arr:
            one = max(one + num, zero)
            zero = max(zero + num, num)
            ans = max(ans, zero, one)
        return ans
