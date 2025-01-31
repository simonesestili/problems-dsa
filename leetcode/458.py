class Solution:
    def poorPigs(self, buckets, die, test):
        return ceil(log(buckets, test // die + 1))
