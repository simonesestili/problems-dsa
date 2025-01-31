class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        if not self.arr:
            self.arr.append(num)
            return
        if num <= self.arr[0]:
            self.arr.insert(0, num)
            return
        elif num >= self.arr[-1]:
            self.arr.append(num)
            return
        left, right = 0, len(self.arr) - 1
        while left < right:
            mid = (left + right) // 2
            if self.arr[mid] >= num:
                right = mid
            else:
                left = mid + 1
        self.arr.insert(left, num)        

    def findMedian(self) -> float:
        if len(self.arr) % 2:
            return self.arr[len(self.arr) // 2]
        return (self.arr[len(self.arr) // 2] + self.arr[len(self.arr) // 2 - 1]) / 2
