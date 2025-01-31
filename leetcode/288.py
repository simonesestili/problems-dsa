class ValidWordAbbr:
    def __init__(self, words):
        self.abbrs = set()
        self.mappings = defaultdict(set)
        for word in words:
            abbr = self.abbreviate(word)
            self.abbrs.add(abbr)
            self.mappings[abbr].add(word)

    def isUnique(self, word):
        abbr = self.abbreviate(word)
        return abbr not in self.abbrs or len(self.mappings[abbr]) == 1 and word in self.mappings[abbr]

    def abbreviate(self, word):
        if len(word) < 3: return word
        return f'{word[0]}{len(word) - 2}{word[-1]}'
