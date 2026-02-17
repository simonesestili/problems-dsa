class Solution:
    def readBinaryWatch(self, on):
        return [f'{h}:{m:02d}' for m in range(60) for h in range(12) if h.bit_count() + m.bit_count() == on]
