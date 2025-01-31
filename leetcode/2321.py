class Solution:
    def maximumsSplicedArray(self, a, b):

        def kadane(arr):
            best = curr = 0
            for x in arr:
                curr = max(curr + x, x)
                best = max(best, curr)
            return best

        return max(sum(a) + kadane([bb - aa for aa, bb in zip(a, b)]), sum(b) + kadane([aa - bb for aa, bb in zip(a, b)]))


