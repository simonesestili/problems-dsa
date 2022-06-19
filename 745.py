class WordFilter:
    def __init__(self, words):
        self.mappings = {}
        for i, word in enumerate(words):
            l = len(word)
            for pre in range(l):
                for suf in range(l):
                    self.mappings[word[:pre+1] + '!' + word[-suf-1:]] = i

    def f(self, prefix, suffix):
        return self.mappings.get((prefix + '!' + suffix), -1)
