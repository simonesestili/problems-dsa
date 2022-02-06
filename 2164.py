class Solution:
    def sortEvenOdd(self, nums):
        odds = sorted([nums[i] for i in range(len(nums)) if i % 2], reverse=True)
        evens = sorted([nums[i] for i in range(len(nums)) if not i % 2])
        ans = []
        for i in range(len(odds)):
            ans.append(evens[i])
            ans.append(odds[i])
        if len(evens) > len(odds): ans.append(evens[-1])
        return ans

