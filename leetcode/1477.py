class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        ans, best, left, curr = float('inf'), [float('inf')] * n, 0, 0
        for right in range(n):
            curr += arr[right]
            while curr > target:
                curr -= arr[left]
                left += 1

            length = float('inf')
            if curr == target and left <= right:
                length = (right - left + 1)
                prev = float('inf') if not left else best[left - 1]
                ans = min(ans, length + prev)
            best[right] = min(float('inf') if not right else best[right - 1], length)

        return -1 if ans == float('inf') else ans
