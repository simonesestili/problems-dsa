class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        globalMax = localMax = len([s[i] for i in range(k) if s[i] in vowels])
        left, right = 0, k
        while right < len(s):
            localMax -= 1 if s[left] in vowels else 0
            localMax += 1 if s[right] in vowels else 0
            left += 1
            right += 1
            globalMax = max(globalMax, localMax)
        return globalMax    
