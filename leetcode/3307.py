class Solution:
    def kthCharacter(self, k, ops):
        ops = ops[:ceil(log2(k))+1]
        inc, size = 0, 2 ** len(ops)
        while ops:
            if k > size // 2:
                inc += ops[-1]
                k -= size // 2
            size //= 2
            ops.pop()
        return chr(ord('a') + inc % 26)
