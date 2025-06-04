class Solution:
    def answerString(self, word, friends):
        return max(word[i:i+len(word)-friends+1] for i in range(len(word))) if friends > 1 else word
