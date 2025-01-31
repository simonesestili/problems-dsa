class Solution:
    def wordCount(self, start, target):
        count = 0
        start, target = set([''.join(sorted(w)) for w in start]), [sorted(w) for w in target]
        for word in target:
            for i in range(len(word)):
                if ''.join(word[:i] + word[i + 1:]) in start:
                    count += 1
                    break
        return count
