class Solution:
    # 4 can be 0b100, 0b10, and 0b1
    # 5 can be 0b1010, and 0b101
    # if we multiply each odd number by 2 it simplifies the problem
    # since the only move we can make on each number is dividing it by 2
    def minimumDeviation(self, nums):
        ans = mn = float('inf')
        n, heap = len(nums), []
        for i in range(n):
            nums[i] <<= nums[i] & 1
            mn = min(mn, nums[i])
            heappush(heap, -nums[i])

        while heap[0] & 1 ^ 1:
            ans = min(ans, -heap[0] - mn)
            mn = min(mn, -heap[0] >> 1)
            heapreplace(heap, heap[0] >> 1)

        return min(ans, -heap[0] - mn)
            
