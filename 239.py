class Solution:
    def maxSlidingWindow(self, nums, k):
        queue, n = MinQueue(), len(nums)
        for i in range(k - 1): queue.enqueue(-nums[i])

        ans = []
        for i in range(k - 1, n):
            queue.enqueue(-nums[i])
            ans.append(-queue.mn())
            queue.dequeue()
        return ans


class MinQueue:
    def __init__(self):
        self.queue = deque([])
        self.mono = deque([])

    def enqueue(self, val):
        self.queue.append(val)
        while self.mono and self.mono[-1] > val:
            self.mono.pop()
        self.mono.append(val)

    def dequeue(self):
        if self.queue.popleft() == self.mono[0]:
            self.mono.popleft()

    def mn(self):
        return self.mono[0]
