class MagicDictionary:
    def buildDict(self, dictionary):
        self.dict = defaultdict(list)
        for word in dictionary:
            self.dict[len(word)].append(word)

    def search(self, target):
        for word in self.dict[len(target)]:
            diffs = 0
            for i in range(len(word)):
                diffs += target[i] != word[i]
            if diffs == 1:
                return True
        return False
