class Solution:
    def maxResult(self, nums, k):
        mono = MaxQueue()
        for i in range(len(nums)):
            nums[i] += mono.mx()
            mono.enqueue(nums[i])
            if mono.length() > k: mono.dequeue()
        return nums[-1]

class MaxQueue:
    def __init__(self):
        self.queue = deque()
        self.mono = deque()

    def enqueue(self, val):
        self.queue.append(val)
        while self.mono and self.mono[-1] < val:
            self.mono.pop()
        self.mono.append(val)

    def dequeue(self):
        if self.queue.popleft() == self.mono[0]:
            self.mono.popleft()

    def mx(self):
        return 0 if not self.mono else self.mono[0]

    def length(self):
        return len(self.queue)
