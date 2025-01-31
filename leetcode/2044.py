# Time: O(2^n)
# This is because at each index of nums we have two choices:
#     Take the element or skip it
# Thus, there will be a total of 2^n subsequences (one of which is empty)
class Solution:
    # Check every single subsequence's OR values
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        vals = []

        def subsets(idx, val):
            if idx == len(nums):
                vals.append(val)
                return
            # When building a subsequence at each index we have two choices
            # We can either take the element at idx and add it to the subsequence
            # Or we can skip the element at idx and not add it
            subsets(idx + 1, val | nums[idx])
            subsets(idx + 1, val)

        subsets(0, 0)
        
        # return the count of subsequences with the max OR value
        return vals.count(max(vals))
