class Solution:
    def numSquares(self, n):
        nums, seen, count = [n], set(), 0
        while True:
            nextNums = []
            for num in nums:
                if not num:
                    return count
                for i in range(1, int(num ** 0.5) + 1):
                    val = num - i ** 2
                    if val not in seen:
                        nextNums.append(val)
                        seen.add(val)
            count += 1
            nums = nextNums
