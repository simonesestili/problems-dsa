class Solution:
    def lengthOfLongestSubstring(self, s):
        n, counts = len(s), defaultdict(int)
        longest = left = 0
        for right in range(n):
            counts[s[right]] += 1
            if self.isNonRepeating(counts):
                longest = max(longest, right - left + 1)
            else:
                while not self.isNonRepeating(counts):
                    counts[s[left]] -= 1
                    left += 1
        return longest                    


    def isNonRepeating(self, counts):
        for key in counts:
            if counts[key] > 1:
                return False
        return True    

