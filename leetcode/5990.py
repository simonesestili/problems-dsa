class Solution:
    def rearrangeArray(self, nums):
        ans, pos, neg = [], [], []
        for x in nums:
            if x > 0: pos.append(x)
            else: neg.append(x)
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans
