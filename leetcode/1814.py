class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        total = 0
        seen = {}
        for num in nums:
            diff = num - self.rev(num)
            if diff in seen:
                total += seen[diff]
            seen[diff] = seen.get(diff, 0) + 1
        return int(total % (1e9 + 7))

    def rev(self, n):
        return int(str(n)[-1::-1])