class Solution:
    def sampleStats(self, count):
        def mode():
            freq = 0
            for i in range(256):
                if count[i] > count[freq]:
                    freq = i
            return freq        

        def get(idx):
            for k in range(256):
                if idx < count[k]:
                    return k
                idx -= count[k]

        total = sum(count)
        minimum = min([k for k in range(256) if count[k]])
        maximum = max([k for k in range(256) if count[k]])
        mean = sum([k * count[k] for k in range(256)]) / total
        median = get(total // 2) if total % 2 else (get(total // 2 - 1) + get(total // 2)) / 2
        mode = mode()
        return [minimum, maximum, mean, median, mode]
