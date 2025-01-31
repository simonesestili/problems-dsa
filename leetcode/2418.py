class Solution:
    def sortPeople(self, names, heights):
        return [name for height, name in sorted(zip(heights, names), reverse=True)]

