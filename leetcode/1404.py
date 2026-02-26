class Solution:
    def numSteps(self, s):
        steps = curr = 0
        for x in reversed(s[1:]):
            curr += int(x == '1')
            steps += curr % 2 + 1
            curr = int(curr > 0)
        return steps + curr
