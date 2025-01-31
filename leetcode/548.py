class Solution:
    def splitArray(self, nums):
        n, self.nums, self.prefix, = len(nums), nums, [0]
        for x in nums: self.prefix.append(self.prefix[-1] + x)
        for j in range(3, n - 3):
            left, right = self.split(0, j - 1), self.split(j + 1, n - 1)
            if (left & right): return True
        return False

    def split(self, i, j): # i, j, k = start of arr, end of arr, split idx
        seen, l, total = set(), self.nums[i], self.sum_query(i, j)
        for k in range(i + 1, j):
            if total - l - self.nums[k] == l:
                seen.add(l)
            l += self.nums[k]
        return seen

    def sum_query(self, i, j):
        return self.prefix[j + 1] - self.prefix[i]
