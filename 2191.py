class Solution:
    def sortJumbled(self, mapping, nums):

        def jumble(num):
            ans = ''.join(str(mapping[int(dig)]) for dig in str(num))
            return int(ans)

        jumbled = sorted([(jumble(num), i) for i, num in enumerate(nums)])
        return [nums[i] for _, i in jumbled]

