class Solution:
    def largestWordCount(self, messages, senders):
        counts = defaultdict(int)
        for msg, snd in zip(messages, senders):
            counts[snd] += msg.count(' ') + 1

        return max(senders, key=lambda s: (counts[s], s))
