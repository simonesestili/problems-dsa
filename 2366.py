class Solution:
    def minimumReplacement(self, nums):
        n, mn = len(nums), nums[-1]
        moves = 0

        for x in nums[-2::-1]:
            if x <= mn:
                mn = x
                continue
            if x % mn == 0:
                moves += x // mn - 1
            else:
                moves += x // mn
                mn = x // (x // mn + 1)

        return moves

