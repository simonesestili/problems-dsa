class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = [0] * 26
        for letter in s1:
            target[ord(letter) - ord('a')] += 1
        
        window = [0] * 26
        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1
        if target == window:
            return True

        left, right = 0, len(s1)
        while right < len(s2):
            window[ord(s2[left]) - ord('a')] -= 1
            left += 1
            window[ord(s2[right]) - ord('a')] += 1
            right += 1
            if target == window:
                return True
        return False