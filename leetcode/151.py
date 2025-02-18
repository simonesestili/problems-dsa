class Solution:
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])
