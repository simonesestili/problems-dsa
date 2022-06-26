class Solution:     
    def maxScore(self, cards, k):
        left = 0
        ans = right = sum(cards[-k:])
        for i in range(k):
            left += cards[i]
            right -= cards[-k+i]
            ans = max(ans, left + right)
        return ans

