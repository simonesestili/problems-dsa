class Solution:
    def numTriplets(self, nums1, nums2):
        self.triplets = 0

        def count(a, b):
            m, n = len(a), len(b)
            for i in range(m):
                seen, target = defaultdict(int), pow(a[i], 2)
                for j in range(n):
                    if target % b[j]: continue
                    self.triplets += seen[target // b[j]]
                    seen[b[j]] += 1

        count(nums1, nums2)
        count(nums2, nums1)
        return self.triplets
