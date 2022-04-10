class Fenwick:
    def __init__(self, arr):
        self.bit = [0] * (len(arr) + 1)
        for i, x in enumerate(arr): self.update(i, x)
        print(self.bit)

    def update(self, idx, val):
        idx += 1
        while idx < len(self.bit):
            self.bit[idx] += val
            idx += idx & -idx

    def query(self, right):
        res, right = 0, right + 1
        while right:
            res += self.bit[right]
            right -= right & -right
        return res

f = Fenwick([3,2,-1,6,5,4,-3,3,7,2,3])
print(f.query(5))
