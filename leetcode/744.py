class Solution:
    def nextGreatestLetter(self, letters, target):
        i = bisect_right(letters, target)
        return letters[i] if i < len(letters) else letters[0]
