class Solution:
    def uniqueOccurrences(self, arr):
        return len(c := Counter(arr)) == len(set(c.values()))
