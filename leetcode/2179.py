class Solution:
    def goodTriplets(self, nums1, nums2):
        idxs = {x: i for i, x in enumerate(nums2)}
        arr = [idxs[x] for x in nums1]

        ans, prefix, suffix = 0, SortedList(), SortedList(arr)
        for x in arr:
            suffix.remove(x)
            l = prefix.bisect_left(x)
            r = len(suffix) - suffix.bisect_right(x)
            ans += l * r
            prefix.add(x)
        return ans
