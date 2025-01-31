class Solution:
    def pathInZigZagTree(self, label):
        path = []
        while label:
            path.append(label)
            if label == 1: break
            label = self.inverse(label >> 1)
        return reversed(path)

    def inverse(self, label):
        curr, c = label, -1
        while curr: curr, c = curr >> 1, c + 1
        return 3 * (1 << c) - label - 1
