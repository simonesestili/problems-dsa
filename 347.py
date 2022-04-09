class Solution:
    def topKFrequent(self, nums, k):
        n, count = len(nums), Counter(nums)
        
        # Each element can have some frequency in the range [1, n]
        buckets = [list() for _ in range(n + 1)]
        for num in count: buckets[count[num]].append(num)

        ans = []
        for freq in range(n, 0, -1):
            while buckets[freq] and len(ans) < k: ans.append(buckets[freq].pop())
            if len(ans) == k: break

        return ans
