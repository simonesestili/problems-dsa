class FindSumPairs:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, idx, val):
        num = self.nums2[idx]
        self.freq[num] -= 1
        self.freq[num + val] += 1
        self.nums2[idx] += val

    def count(self, tot):
        count = 0
        for num in self.nums1:
            count += self.freq[tot - num]
        return count
