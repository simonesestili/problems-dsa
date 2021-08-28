class Solution:     
	def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        indicies = []
        target = [0] * 26
        current = [0] * 26
        # Fill the target count of letters
        for letter in p:
            target[ord(letter) - ord('a')] += 1
        start, end = 0, 0
        while end < len(p):
            current[ord(s[end]) - ord('a')] += 1
            end += 1
        if target == current:
            indicies.append(0)

        while end < len(s):
            current[ord(s[start]) - ord('a')] -= 1
            start += 1
            current[ord(s[end]) - ord('a')] += 1
            end += 1
            if target == current:
                indicies.append(start)
        return indicies
