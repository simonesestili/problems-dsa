class Solution:
    def reverseWords(self, s):
        return ' '.join([word for word in ''.join(' '.join(s.split())).split()[::-1]])
