class Solution:
    def minimumRefill(self, plants, a, b):
        n = len(plants)
        left, right = 0, n - 1
        A, B = a, b
        ans = 0
        while left < right:
            if A < plants[left]:
                A = a
                ans += 1
            A -= plants[left]
            left += 1

            if B < plants[right]:
                B = b
                ans += 1
            B -= plants[right]
            right -= 1

        if left != right or A >= plants[left] or B >= plants[left]: return ans
        return ans + 1
