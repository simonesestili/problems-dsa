class Encrypter:
    def __init__(self, keys, vals, d):
        self.d = d
        self.pair = {}
        self.rev = defaultdict(set)
        for k, v in zip(keys, vals):
            self.rev[v].add(k)
            self.pair[k] = v
        
    def encrypt(self, word1):
        return ''.join([self.pair[c] for c in word1])

    def decrypt(self, word2):
        parts = [word2[i:i+2] for i in range(0, len(word2), 2)]

        def valid(w):
            if len(w) * 2 != len(word2): return False
            for part, c in zip(parts, w):
                if c not in self.rev[part]: return False
            return True

        return sum(valid(orig) for orig in self.d)
