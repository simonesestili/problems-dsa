# Q2
class Solution:
    def maximumSubsequenceCount(self, text, pattern):
        a, b = pattern[0], pattern[1]
        seen, rem = 0, text.count(b)

        total = extra = 0
        for c in text:
            rem -= c == b
            total += int(c == a) * rem
            seen += c == a
            extra = max(extra, seen, rem)

        text = a + text
        rem = text.count(b)
        new = 0

        # check for case where we prepend a to text
        for c in text:
            rem -= c == b
            new += int(c == a) * rem

        return max(total + extra, new)
