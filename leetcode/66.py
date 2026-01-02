class Solution:
    def plusOne(self, digits):
        digits[-1] += 1
        ans, curr = [], 0
        for d in reversed(digits):
            curr, rem = divmod(curr + d, 10)
            ans.append(rem)
        if curr:
            ans.append(curr)
        return ans[::-1]
