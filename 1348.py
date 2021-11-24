class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class BST:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        curr = self.root
        while True:
            if val <= curr.val:
                if not curr.left:
                    curr.left = Node(val)
                    return
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = Node(val)
                    return
                curr = curr.right

    def get_sorted(self):
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(self.root)
        return res

class TweetCounts:
    def __init__(self):
        self.tweets = {}
        self.freqs = {'minute': 60, 'hour': 60 * 60, 'day': 60 * 60 * 24}

    def recordTweet(self, tweetName, time):
        if tweetName not in self.tweets:
            self.tweets[tweetName] = BST(time)
        else:
            self.tweets[tweetName].insert(time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        if tweetName not in self.tweets:
            return []
        tweets = self.tweets[tweetName].get_sorted()
        freq = self.freqs[freq]
        res = [0] * ((endTime - startTime) // freq + 1)
        left, right = bisect_left(tweets, startTime), bisect_right(tweets, endTime)
        for i in range(left, right):
            res[(tweets[i] - startTime) // freq] += 1
        return res

