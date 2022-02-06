class Solution:
    def pivotArray(self, nums, val):
        less, more = [], []
        equal = 0
        for x in nums:
            if x < val: less.append(x)
            elif x > val: more.append(x)
            else: equal += 1
        return less + [val] * equal + more
