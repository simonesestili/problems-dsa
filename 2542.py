class Solution:
    def maxScore(self, nums1, nums2, k):
        mins = defaultdict(list)
        for a, b in zip(nums1, nums2):
            mins[b].append(a)

        ans, total, heap = 0, 0, []
        for mn, vals in sorted(mins.items(), reverse=True):
            for val in vals:
                if len(heap) == k and val < heap[0]: continue
                if len(heap) == k:
                    total -= heappop(heap)
                heappush(heap, val)
                total += val
            if len(heap) == k:
                ans = max(ans, total * mn)
        return ans
