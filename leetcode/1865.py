class FindSumPairs:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnts = Counter(nums2)

    def add(self, i, val):
        self.cnts[self.nums2[i]] -= 1
        self.nums2[i] += val
        self.cnts[self.nums2[i]] += 1

    def count(self, tot):
        return sum(self.cnts[tot - x] for x in self.nums1)
